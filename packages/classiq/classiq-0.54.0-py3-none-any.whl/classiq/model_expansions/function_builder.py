from collections.abc import Iterable, Iterator, Sequence
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Generic, Optional, TypeVar

from classiq.interface.exceptions import (
    ClassiqExpansionError,
    ClassiqInternalExpansionError,
)
from classiq.interface.generator.compiler_keywords import (
    EXPANDED_KEYWORD,
    LAMBDA_KEYWORD,
)
from classiq.interface.generator.functions.builtins.internal_operators import (
    WITHIN_APPLY_NAME,
)
from classiq.interface.generator.functions.port_declaration import (
    PortDeclarationDirection,
)
from classiq.interface.model.model import MAIN_FUNCTION_NAME
from classiq.interface.model.native_function_definition import (
    FunctionSynthesisData,
    NativeFunctionDefinition,
)
from classiq.interface.model.port_declaration import PortDeclaration
from classiq.interface.model.quantum_function_declaration import (
    PositionalArg,
)
from classiq.interface.model.quantum_statement import QuantumStatement

from classiq.model_expansions.capturing.captured_var_manager import update_captured_vars
from classiq.model_expansions.capturing.mangling_utils import demangle_name
from classiq.model_expansions.closure import Closure, FunctionClosure

ClosureType = TypeVar("ClosureType", bound=Closure)


@dataclass
class Block:
    statements: list[QuantumStatement] = field(default_factory=list)
    captured_vars: list[PortDeclaration] = field(default_factory=list)


@dataclass
class OperationContext(Generic[ClosureType]):
    closure: ClosureType
    blocks: dict[str, Block] = field(default_factory=dict)

    @property
    def name(self) -> str:
        return self.closure.name

    @property
    def positional_arg_declarations(self) -> Sequence[PositionalArg]:
        return self.closure.positional_arg_declarations

    def statements(self, block_name: str) -> list[QuantumStatement]:
        return self.blocks[block_name].statements


@dataclass
class FunctionContext(OperationContext[FunctionClosure]):
    @classmethod
    def create(cls, original_function: FunctionClosure) -> "FunctionContext":
        return cls(original_function, {"body": Block()})

    @property
    def body(self) -> list[QuantumStatement]:
        return self.statements("body")

    @property
    def captured_vars(self) -> list[PortDeclaration]:
        return self.blocks["body"].captured_vars

    @property
    def is_lambda(self) -> bool:
        return self.closure.is_lambda

    @property
    def synthesis_data(self) -> FunctionSynthesisData:
        return self.closure.synthesis_data


class OperationBuilder:
    def __init__(self) -> None:
        self._operations: list[OperationContext] = []
        self._blocks: list[str] = []
        self._counter = 0

    @property
    def current_operation(self) -> Closure:
        return self._operations[-1].closure

    @property
    def current_function(self) -> FunctionClosure:
        for operation in reversed(self._operations):
            if isinstance(operation.closure, FunctionClosure):
                return operation.closure
        raise ClassiqInternalExpansionError("No function found")

    @property
    def _current_statements(self) -> list[QuantumStatement]:
        return self._operations[-1].blocks[self._blocks[-1]].statements

    def emit_statement(self, statement: QuantumStatement) -> None:
        self._current_statements.append(statement)

    @property
    def current_statement(self) -> QuantumStatement:
        return self._current_statements[-1]

    def add_captured_vars(self, captured_vars: Iterable[PortDeclaration]) -> None:
        self._operations[-1].blocks[self._blocks[-1]].captured_vars.extend(
            captured_vars
        )

    @contextmanager
    def block_context(self, block_name: str) -> Iterator[None]:
        self._blocks.append(block_name)
        self._operations[-1].blocks[block_name] = Block()
        yield
        self._blocks.pop()

    @contextmanager
    def operation_context(
        self, original_operation: Closure
    ) -> Iterator[OperationContext]:
        context: OperationContext
        if isinstance(original_operation, FunctionClosure):
            context = FunctionContext.create(original_operation)
        else:
            context = OperationContext(closure=original_operation)
        self._operations.append(context)
        yield context
        self._update_captured_vars()
        self._operations.pop()

    def _update_captured_vars(self) -> None:
        for block in self._operations[-1].blocks.values():
            block.captured_vars = update_captured_vars(block.captured_vars)
            if not self._is_within_apply_context():
                validate_captured_vars(block.captured_vars)

    def is_compute_context(self) -> bool:
        return self._is_within_apply_context("within")

    def _is_within_apply_context(self, block_name: Optional[str] = None) -> bool:
        return self._is_op_within_apply_context(block_name, -1) or (
            len(self._operations) > 1
            and isinstance(self._operations[-1], FunctionContext)
            and self._is_op_within_apply_context(block_name, -2)
        )

    def _is_op_within_apply_context(
        self, block_name: Optional[str], index: int
    ) -> bool:
        return self._operations[index].name == WITHIN_APPLY_NAME and (
            block_name is None or self._blocks[index] == block_name
        )

    def create_definition(
        self, function_context: FunctionContext
    ) -> NativeFunctionDefinition:
        name = function_context.name
        if name != MAIN_FUNCTION_NAME:
            name = f"{name}_{LAMBDA_KEYWORD + '_0_0_' if function_context.is_lambda else ''}{EXPANDED_KEYWORD}_{self._counter}"
            self._counter += 1

        new_parameters: list[PortDeclaration] = [
            param
            for param in function_context.positional_arg_declarations
            if isinstance(param, PortDeclaration)
        ] + function_context.captured_vars

        return NativeFunctionDefinition(
            name=name,
            body=function_context.body,
            positional_arg_declarations=new_parameters,
            synthesis_data=function_context.synthesis_data,
        )


def validate_captured_vars(captured_vars: list[PortDeclaration]) -> None:
    if input_captured := [
        demangle_name(var.name)
        for var in captured_vars
        if var.direction is PortDeclarationDirection.Input
    ]:
        raise ClassiqExpansionError(
            f"Captured quantum variables {input_captured!r} cannot be used as inputs"
        )
    if output_captured := [
        demangle_name(var.name)
        for var in captured_vars
        if var.direction is PortDeclarationDirection.Output
    ]:
        raise ClassiqExpansionError(
            f"Captured quantum variables {output_captured!r} cannot be used as outputs"
        )
