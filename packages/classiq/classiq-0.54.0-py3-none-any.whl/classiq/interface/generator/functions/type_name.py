from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Optional

import pydantic

from classiq.interface.generator.expressions.qmod_qstruct_proxy import QmodQStructProxy
from classiq.interface.generator.functions.classical_type import (
    ClassicalType,
)
from classiq.interface.helpers.pydantic_model_helpers import values_with_discriminator
from classiq.interface.model.handle_binding import HandleBinding
from classiq.interface.model.quantum_type import (
    QuantumType,
)

if TYPE_CHECKING:
    from classiq.interface.generator.functions.concrete_types import ConcreteQuantumType


class TypeName(ClassicalType, QuantumType):
    kind: Literal["struct_instance"]
    name: str = pydantic.Field(description="The type name of the instance")
    _assigned_fields: Optional[Mapping[str, "ConcreteQuantumType"]] = (
        pydantic.PrivateAttr(default=None)
    )

    @pydantic.model_validator(mode="before")
    @classmethod
    def _set_kind(cls, values: Any) -> dict[str, Any]:
        return values_with_discriminator(values, "kind", "struct_instance")

    def _update_size_in_bits_from_declaration(self) -> None:
        fields_types = list(self.fields.values())
        for field_type in fields_types:
            field_type._update_size_in_bits_from_declaration()
        if all(field_type.has_size_in_bits for field_type in fields_types):
            self._size_in_bits = sum(
                field_type.size_in_bits for field_type in fields_types
            )

    def get_proxy(self, handle: "HandleBinding") -> "QmodQStructProxy":
        from classiq.interface.generator.expressions.qmod_qstruct_proxy import (
            QmodQStructProxy,
        )

        return QmodQStructProxy(
            handle=handle, struct_name=self.name, fields=self.fields
        )

    @property
    def qmod_type_name(self) -> str:
        return self.name

    @property
    def type_name(self) -> str:
        return self.name

    @property
    def fields(self) -> Mapping[str, "ConcreteQuantumType"]:
        from classiq.qmod.model_state_container import QMODULE

        if self._assigned_fields is None:
            qstruct_fields = QMODULE.qstruct_decls[self.name].fields
            self._assigned_fields = {
                field_name: field_type.model_copy()
                for field_name, field_type in qstruct_fields.items()
            }

        return self._assigned_fields

    def _set_fields(self, fields: Mapping[str, "ConcreteQuantumType"]) -> None:
        self._assigned_fields = fields


class Enum(TypeName):
    pass


class Struct(TypeName):
    pass
