from typing import TYPE_CHECKING, Literal

import pydantic

from classiq.interface.model.quantum_expressions.quantum_expression import (
    QuantumExpressionOperation,
)

if TYPE_CHECKING:
    from classiq.interface.model.statement_block import StatementBlock


class Control(QuantumExpressionOperation):
    kind: Literal["Control"]
    body: "StatementBlock"

    _ctrl_size: int = pydantic.PrivateAttr(default=0)

    @property
    def ctrl_size(self) -> int:
        return self._ctrl_size

    def set_ctrl_size(self, ctrl_size: int) -> None:
        self._ctrl_size = ctrl_size
