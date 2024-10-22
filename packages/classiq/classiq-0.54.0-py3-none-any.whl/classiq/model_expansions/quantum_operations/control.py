from sympy import Equality
from sympy.logic.boolalg import Boolean
from typing_extensions import TypeGuard

from classiq.interface.exceptions import (
    ClassiqExpansionError,
    ClassiqInternalExpansionError,
)
from classiq.interface.generator.compiler_keywords import INPLACE_ARITH_AUX_VAR_PREFIX
from classiq.interface.generator.expressions.expression import Expression
from classiq.interface.generator.expressions.expression_types import ExpressionValue
from classiq.interface.generator.expressions.qmod_qscalar_proxy import QmodQNumProxy
from classiq.interface.generator.expressions.qmod_sized_proxy import QmodSizedProxy
from classiq.interface.generator.functions.builtins.internal_operators import (
    CONTROL_OPERATOR_NAME,
)
from classiq.interface.model.bind_operation import BindOperation
from classiq.interface.model.control import Control
from classiq.interface.model.handle_binding import HANDLE_ID_SEPARATOR, HandleBinding
from classiq.interface.model.quantum_expressions.arithmetic_operation import (
    ArithmeticOperation,
    ArithmeticOperationKind,
)
from classiq.interface.model.quantum_type import QuantumBit, QuantumBitvector
from classiq.interface.model.statement_block import ConcreteQuantumStatement
from classiq.interface.model.variable_declaration_statement import (
    VariableDeclarationStatement,
)
from classiq.interface.model.within_apply_operation import WithinApply

from classiq.model_expansions.capturing.propagated_var_stack import (
    validate_args_are_not_propagated,
)
from classiq.model_expansions.closure import Closure
from classiq.model_expansions.evaluators.control import (
    resolve_num_condition,
    type_name,
)
from classiq.model_expansions.quantum_operations.expression_operation import (
    ExpressionOperationEmitter,
)
from classiq.model_expansions.scope import Scope

ARRAY_CAST_SUFFIX = HANDLE_ID_SEPARATOR + "array_cast"


class ControlEmitter(ExpressionOperationEmitter[Control]):
    def emit(self, control: Control, /) -> None:
        condition = self._evaluate_op_expression(control)
        control = control.model_copy(update=dict(expression=condition))

        arrays_with_subscript = self._get_symbols_to_split(condition)
        if len(arrays_with_subscript) > 0:
            self._emit_with_split(control, condition, arrays_with_subscript)
            return

        condition_val = condition.value.value
        if isinstance(condition_val, QmodSizedProxy):
            self._validate_canonical_condition(condition_val)
            self._emit_canonical_control(control)
            return

        self._validate_condition(condition_val)
        self._emit_with_boolean(control)

    def _emit_canonical_control(self, control: Control) -> None:
        # canonical means control(q, body) where q is a single quantum variable
        control = self._evaluate_types_in_expression(control, control.expression)
        with self._propagated_var_stack.capture_variables(control):
            self._emit_propagated(control)

    def _emit_propagated(self, control: Control) -> None:
        if control.is_generative():
            context = self._register_generative_context(control, CONTROL_OPERATOR_NAME)
            control = control.model_copy(update={"body": context.statements("body")})

        if self._should_wrap_control(control):
            self._emit_wrapped(control)
            return
        self._emit_as_operation(control)

    def _should_wrap_control(self, control: Control) -> bool:
        # TODO we can return back to the general case (as in _should_wrap function)
        #  once we implement the "smart control" pass to blocks:
        #  Control(q, body) -> WithinApply(
        #       compute=aux:=QBit(), allocate(1, aux), Control(q, [X(aux)]),
        #       action=Control(aux, body)
        #  )
        #  We also need to be able to nest multiple Control statements to a single one
        return len(control.body) > 1

    def _emit_as_operation(self, control: Control) -> None:
        control_operation = Closure(
            name=CONTROL_OPERATOR_NAME,
            blocks=dict(body=control.body),
            scope=Scope(parent=self._current_scope),
        )
        context = self._expand_operation(control_operation)
        validate_args_are_not_propagated(
            control.var_handles,
            self._propagated_var_stack.get_propagated_variables(),
        )
        self._update_control_state(control)
        self._builder.emit_statement(
            control.model_copy(update=dict(body=context.statements("body")))
        )

    def _emit_wrapped(self, control: Control) -> None:
        wrapping_function = self._create_expanded_wrapping_function(
            CONTROL_OPERATOR_NAME, control.body
        )
        validate_args_are_not_propagated(
            control.var_handles,
            self._propagated_var_stack.get_propagated_variables(),
        )
        self._update_control_state(control)
        self._builder.emit_statement(
            control.model_copy(update=dict(body=[wrapping_function]))
        )

    @staticmethod
    def _update_control_state(control: Control) -> None:
        condition_val = control.expression.value.value
        if not isinstance(condition_val, QmodSizedProxy):
            raise ClassiqInternalExpansionError("Control is not in canonical form")
        control.set_ctrl_size(condition_val.size)

    def _emit_with_boolean(self, control: Control) -> None:
        condition_val = control.expression.value.value
        if self._is_simple_equality(condition_val):
            ctrl, ctrl_state = resolve_num_condition(condition_val)
            self._emit_with_x_gates(control, ctrl, ctrl_state)
        else:
            self._emit_with_arithmetic(control)

    @staticmethod
    def _is_simple_equality(condition_val: ExpressionValue) -> TypeGuard[Equality]:
        # Note that we don't support equalities with non-integer values yet
        return isinstance(condition_val, Equality) and (
            (
                condition_val.args[0].is_Atom
                and not isinstance(condition_val.args[0], QmodSizedProxy)
                and isinstance(condition_val.args[1], QmodSizedProxy)
            )
            or (
                condition_val.args[1].is_Atom
                and not isinstance(condition_val.args[1], QmodSizedProxy)
                and isinstance(condition_val.args[0], QmodSizedProxy)
            )
        )

    def _create_canonical_control_op(
        self, control: Control, handle_name: str
    ) -> Control:
        handle_expr = self._interpreter.evaluate(Expression(expr=handle_name)).emit()
        return control.model_copy(update=dict(expression=handle_expr))

    def _emit_with_x_gates(
        self, control: Control, ctrl: QmodSizedProxy, ctrl_state: str
    ) -> None:
        compute_op: list[ConcreteQuantumStatement] = []

        x_gate_value = self._get_x_gate_value(ctrl_state)
        if x_gate_value != 0:
            compute_op.append(
                ArithmeticOperation(
                    result_var=ctrl.handle,
                    expression=Expression(expr=str(x_gate_value)),
                    operation_kind=ArithmeticOperationKind.InplaceXor,
                )
            )

        if isinstance(ctrl, QmodQNumProxy):
            # Canonical control does not accept QNum, so we have to cast it
            cast_decl, bind_op = self._get_array_cast_ops(ctrl)
            self._interpreter.emit_statement(cast_decl)
            compute_op.append(bind_op)
            control_op = self._create_canonical_control_op(control, str(cast_decl.name))
        else:
            control_op = self._create_canonical_control_op(control, str(ctrl.handle))

        self._interpreter.emit_statement(
            WithinApply(compute=compute_op, action=[control_op])
        )

    @staticmethod
    def _get_x_gate_value(ctrl_state: str) -> int:
        x_gate_value = 0
        for idx, bit in enumerate(ctrl_state):
            x_gate_value += int(bit == "0") << idx
        return x_gate_value

    def _get_array_cast_ops(
        self, ctrl: QmodQNumProxy
    ) -> tuple[VariableDeclarationStatement, BindOperation]:
        array_cast = self._counted_name_allocator.allocate(
            f"{ctrl.handle}{ARRAY_CAST_SUFFIX}"
        )
        cast_decl = VariableDeclarationStatement(
            name=array_cast, quantum_type=QuantumBitvector()
        )
        bind_op = BindOperation(
            in_handles=[ctrl.handle], out_handles=[HandleBinding(name=array_cast)]
        )
        return cast_decl, bind_op

    def _emit_with_arithmetic(self, control: Control) -> None:
        aux_var = self._counted_name_allocator.allocate(INPLACE_ARITH_AUX_VAR_PREFIX)
        self._interpreter.emit_statement(
            VariableDeclarationStatement(name=aux_var, quantum_type=QuantumBit())
        )
        arith_expression = ArithmeticOperation(
            result_var=HandleBinding(name=aux_var),
            expression=control.expression,
            operation_kind=ArithmeticOperationKind.Assignment,
        )
        self._interpreter.emit_statement(
            WithinApply(
                compute=[arith_expression],
                action=[self._create_canonical_control_op(control, aux_var)],
            )
        )

    @staticmethod
    def _validate_condition(condition_val: ExpressionValue) -> None:
        if not isinstance(condition_val, Boolean):
            raise ClassiqExpansionError(_condition_err_msg(condition_val))

    @staticmethod
    def _validate_canonical_condition(condition_val: ExpressionValue) -> None:
        if isinstance(condition_val, QmodQNumProxy):
            raise ClassiqExpansionError(_condition_err_msg(condition_val))


def _condition_err_msg(condition_val: ExpressionValue) -> str:
    return (
        f"Control condition {str(condition_val)!r} must be a qubit, an array of "
        f"qubits, or a boolean expression, but is {type_name(condition_val)}"
    )
