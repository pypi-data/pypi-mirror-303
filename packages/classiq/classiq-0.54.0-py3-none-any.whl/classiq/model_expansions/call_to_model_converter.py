import dataclasses
import json
from collections.abc import Iterator, Sequence
from functools import cached_property
from typing import Any, Union

from typing_extensions import Self

from classiq.interface.exceptions import ClassiqExpansionError
from classiq.interface.generator.expressions.expression import Expression
from classiq.interface.generator.functions.port_declaration import (
    PortDeclarationDirection,
)
from classiq.interface.model.handle_binding import HandleBinding
from classiq.interface.model.model import MAIN_FUNCTION_NAME, Model
from classiq.interface.model.native_function_definition import NativeFunctionDefinition
from classiq.interface.model.port_declaration import PortDeclaration
from classiq.interface.model.quantum_function_call import ArgValue, QuantumFunctionCall
from classiq.interface.model.quantum_function_declaration import (
    PositionalArg,
    QuantumOperandDeclaration,
)
from classiq.interface.model.quantum_type import QuantumType

from classiq import ClassicalParameterDeclaration
from classiq.model_expansions.scope import Evaluated, QuantumSymbol, evaluated_to_str


@dataclasses.dataclass(frozen=False)
class BlockFunctionInfo:
    block_id: str
    model: Model
    inputs: set[str]
    outputs: set[str]
    inouts: set[str]
    calls: set[str] = dataclasses.field(default_factory=set)

    @classmethod
    def from_call_converter(cls, call_converter: "CallToModelConverter") -> Self:
        return cls(
            block_id=call_converter.block_id,
            model=call_converter.convert(),
            inputs=set(call_converter.call.wiring_inputs),
            outputs=set(call_converter.call.wiring_outputs),
            inouts=set(call_converter.call.wiring_inouts),
        )


class CallToModelConverter:

    def __init__(
        self,
        call: QuantumFunctionCall,
        positional_arg_declarations: Sequence[PositionalArg],
        evaluated_arg: dict[str, Evaluated],
        model: Model,
    ) -> None:
        self.call = call
        self._positional_arg_declarations = positional_arg_declarations
        self._evaluated_arg = evaluated_arg

        self._model = model

    @cached_property
    def block_id(self) -> str:
        args_signature: dict = {}
        for arg_declaration, evaluated_arg in zip(
            self._positional_arg_declarations,
            self._evaluated_arg.values(),
        ):
            args_signature |= _get_arg_signature(arg_declaration, evaluated_arg)
        return f"{self.call.func_name}__{json.dumps(args_signature)}"

    def convert(self) -> Model:
        return self._model.model_copy(
            update={"functions": self._update_model_functions()}
        )

    def _update_model_functions(self) -> list[NativeFunctionDefinition]:
        return [
            (
                self._create_new_main_function()
                if function.name == MAIN_FUNCTION_NAME
                else (
                    function.model_copy(update={"synthesis_data": None})
                    if function.name == self.call.function
                    else function
                )
            )
            for function in self._model.functions
        ]

    def _create_new_main_function(self) -> NativeFunctionDefinition:
        return NativeFunctionDefinition(
            name=MAIN_FUNCTION_NAME,
            positional_arg_declarations=self._make_all_ports_outputs(),
            body=[*self._allocate_ports(), self._update_call()],
        )

    def _make_all_ports_outputs(self) -> list[PortDeclaration]:
        return [
            _convert_port_to_output(port_declaration)
            for port_declaration in self._positional_arg_declarations
            if isinstance(port_declaration, PortDeclaration)
        ]

    def _allocate_ports(self) -> Iterator[QuantumFunctionCall]:
        return (
            QuantumFunctionCall(
                function="allocate",
                positional_args=[
                    self._get_allocation_size(port_declaration.name),
                    HandleBinding(name=port_declaration.name),
                ],
            )
            for port_declaration in self._positional_arg_declarations
            if isinstance(port_declaration, PortDeclaration)
            and port_declaration.direction != PortDeclarationDirection.Output
        )

    def _get_allocation_size(self, port_declara_name: str) -> Expression:
        port_value = self._evaluated_arg[port_declara_name].value
        return Expression(expr=_get_reg_size(port_value, port_declara_name))

    def _update_call(self) -> QuantumFunctionCall:
        return self.call.model_copy(
            update={"positional_args": self._evaluate_positional_args()}
        )

    def _evaluate_positional_args(self) -> list[ArgValue]:
        return [
            _get_positional_arg(arg, evaluated_arg)
            for arg, evaluated_arg in zip(
                self._positional_arg_declarations,
                self._evaluated_arg.values(),
            )
        ]


def _validate_quantum_type(port: Any, port_declara_name: str) -> QuantumType:
    if not isinstance(port, QuantumSymbol):
        raise ClassiqExpansionError(f"Port {port_declara_name!r} has incorrect type")
    return port.quantum_type


def _get_reg_size(port: Any, port_declara_name: str) -> str:
    quantum_type = _validate_quantum_type(port, port_declara_name)
    return str(quantum_type.size_in_bits)


def _get_arg_signature(
    arg_declaration: PositionalArg, evaluated_arg: Evaluated
) -> dict[str, str]:
    arg_value = evaluated_arg.value
    arg_name = arg_declaration.name
    if isinstance(arg_declaration, ClassicalParameterDeclaration):
        return {arg_name: evaluated_to_str(arg_value)}
    if isinstance(arg_declaration, PortDeclaration):
        quantum_type = _validate_quantum_type(arg_value, arg_name)
        return {
            arg_name: quantum_type.model_dump_json(exclude_none=True, exclude={"name"})
        }
    if isinstance(arg_declaration, QuantumOperandDeclaration):
        raise NotImplementedError(
            f"Synthesize separately does not support input operand: {arg_declaration.name!r}"
        )


def _get_positional_arg(
    arg_declaration: PositionalArg, evaluated_arg: Evaluated
) -> Union[Expression, HandleBinding]:
    if isinstance(arg_declaration, ClassicalParameterDeclaration):
        return Expression(expr=evaluated_to_str(evaluated_arg.value))
    if isinstance(arg_declaration, PortDeclaration):
        return HandleBinding(name=arg_declaration.name)
    if isinstance(arg_declaration, QuantumOperandDeclaration):
        raise NotImplementedError(
            f"Synthesize separately does not support input operand: {arg_declaration.name!r}"
        )


def _convert_port_to_output(port: PortDeclaration) -> PortDeclaration:
    if port.direction == PortDeclarationDirection.Output:
        return port
    elif port.direction == PortDeclarationDirection.Inout:
        return port.model_copy(update={"direction": PortDeclarationDirection.Output})
    else:
        raise NotImplementedError(
            f"Synthesize separately does not support input ports: {port.name!r}"
        )
