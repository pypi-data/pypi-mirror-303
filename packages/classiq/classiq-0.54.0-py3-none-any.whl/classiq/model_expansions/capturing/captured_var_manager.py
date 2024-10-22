from classiq.interface.generator.functions.port_declaration import (
    PortDeclarationDirection,
)
from classiq.interface.model.port_declaration import PortDeclaration


def update_captured_vars(captured_vars: list[PortDeclaration]) -> list[PortDeclaration]:
    if not captured_vars:
        return []
    return _update_declarations(captured_vars)


def _update_declarations(
    captured_vars: list[PortDeclaration],
) -> list[PortDeclaration]:
    updated_vars: dict[str, PortDeclaration] = {
        var.name: PortDeclaration(
            name=var.name,
            quantum_type=var.quantum_type,
            direction=PortDeclarationDirection.Inout,
        )
        for var in captured_vars
    }
    for var in captured_vars:
        updated_vars[var.name].direction = _update_var_declaration(
            var.direction, updated_vars[var.name].direction
        )
    return list(updated_vars.values())


def _update_var_declaration(
    stmt_direction: PortDeclarationDirection,
    existing_direction: PortDeclarationDirection,
) -> PortDeclarationDirection:
    if stmt_direction is PortDeclarationDirection.Input:
        if existing_direction is PortDeclarationDirection.Output:
            # This will fail semantically because the inout variable is not initialized.
            # We will get rid of this scenario by unifying variable declaration and allocation.
            return PortDeclarationDirection.Inout
        else:
            return PortDeclarationDirection.Input
    elif stmt_direction is PortDeclarationDirection.Output:
        if existing_direction is PortDeclarationDirection.Input:
            return PortDeclarationDirection.Inout
        else:
            return PortDeclarationDirection.Output
    else:
        return PortDeclarationDirection.Inout
