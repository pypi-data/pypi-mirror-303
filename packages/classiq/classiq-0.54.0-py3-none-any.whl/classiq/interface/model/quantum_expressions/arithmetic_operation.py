from collections.abc import Mapping, Sequence
from typing import Literal, Optional

import pydantic
from pydantic_core.core_schema import ValidationInfo

from classiq.interface.enum_utils import StrEnum
from classiq.interface.generator.arith.arithmetic import (
    ARITHMETIC_EXPRESSION_RESULT_NAME,
    compute_arithmetic_result_type,
)
from classiq.interface.model.handle_binding import (
    ConcreteHandleBinding,
    HandleBinding,
)
from classiq.interface.model.quantum_expressions.quantum_expression import (
    QuantumAssignmentOperation,
)
from classiq.interface.model.quantum_statement import HandleMetadata
from classiq.interface.model.quantum_type import QuantumType


class ArithmeticOperationKind(StrEnum):
    InplaceAdd = "inplace_add"
    Assignment = "assignment"
    InplaceXor = "inplace_xor"


class ArithmeticOperation(QuantumAssignmentOperation):
    kind: Literal["ArithmeticOperation"]

    inplace_result: Optional[bool] = pydantic.Field(
        description="Determines whether the result variable is initialized",
        default=None,
        exclude=True,
    )

    operation_kind: ArithmeticOperationKind = pydantic.Field(
        default=None, validate_default=True
    )

    @pydantic.field_validator("operation_kind", mode="before")
    @classmethod
    def _propagate_inplace_result(
        cls, operation_kind: Optional[ArithmeticOperationKind], info: ValidationInfo
    ) -> ArithmeticOperationKind:
        if operation_kind is None:
            operation_kind = (
                ArithmeticOperationKind.InplaceXor
                if info.data["inplace_result"]
                else ArithmeticOperationKind.Assignment
            )
        return operation_kind

    @property
    def is_inplace(self) -> bool:
        return self.operation_kind in (
            ArithmeticOperationKind.InplaceXor,
            ArithmeticOperationKind.InplaceAdd,
        )

    def initialize_var_types(
        self,
        var_types: dict[str, QuantumType],
        machine_precision: int,
    ) -> None:
        super().initialize_var_types(var_types, machine_precision)
        self._result_type = compute_arithmetic_result_type(
            self.expression.expr, var_types, machine_precision
        )

    @property
    def wiring_inouts(
        self,
    ) -> Mapping[str, ConcreteHandleBinding]:
        inouts = dict(super().wiring_inouts)
        if self.is_inplace:
            inouts[self.result_name()] = self.result_var
        return inouts

    @property
    def readable_inouts(self) -> Sequence[HandleMetadata]:
        inouts = [
            HandleMetadata(handle=handle, readable_location="in an expression")
            for handle in self.var_handles
        ]
        if self.is_inplace:
            inouts.append(
                HandleMetadata(
                    handle=self.result_var,
                    readable_location="on the left-hand side of an in-place assignment",
                )
            )
        return inouts

    @property
    def wiring_outputs(self) -> Mapping[str, HandleBinding]:
        if self.is_inplace:
            return {}
        return super().wiring_outputs

    @property
    def readable_outputs(self) -> Sequence[HandleMetadata]:
        if self.is_inplace:
            return []
        return [
            HandleMetadata(
                handle=self.result_var,
                readable_location="on the left-hand side of an assignment",
            )
        ]

    @classmethod
    def result_name(cls) -> str:
        return ARITHMETIC_EXPRESSION_RESULT_NAME
