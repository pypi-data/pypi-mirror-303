from classiq.interface.generator.functions.builtins.internal_operators import (
    COMPUTE_OPERATOR_NAME,
    WITHIN_APPLY_NAME,
)
from classiq.interface.model.within_apply_operation import WithinApply

from classiq.model_expansions.closure import Closure
from classiq.model_expansions.quantum_operations.emitter import Emitter
from classiq.model_expansions.scope import Scope


class WithinApplyEmitter(Emitter[WithinApply]):
    def emit(self, within_apply: WithinApply, /) -> None:
        with self._propagated_var_stack.capture_variables(within_apply):
            self._emit_propagated(within_apply)

    def _emit_propagated(self, within_apply: WithinApply) -> None:
        if within_apply.is_generative():
            within_apply_context = self._register_generative_context(
                within_apply, WITHIN_APPLY_NAME, ["within", "apply"]
            )
            within_apply = within_apply.model_copy(
                update={
                    "compute": within_apply_context.statements("within"),
                    "action": within_apply_context.statements("apply"),
                }
            )

        if self._should_wrap(within_apply.compute):
            self._emit_wrapped(within_apply)
            return

        self._emit_as_operation(within_apply)

    def _emit_as_operation(self, within_apply: WithinApply) -> None:
        within_apply_operation = Closure(
            name=WITHIN_APPLY_NAME,
            blocks=dict(within=within_apply.compute, apply=within_apply.action),
            scope=Scope(parent=self._current_scope),
        )
        context = self._expand_operation(within_apply_operation)
        self._builder.emit_statement(
            WithinApply(
                compute=context.statements("within"),
                action=context.statements("apply"),
                source_ref=within_apply.source_ref,
            )
        )

    def _emit_wrapped(self, within_apply: WithinApply) -> None:
        wrapped_compute = self._create_expanded_wrapping_function(
            COMPUTE_OPERATOR_NAME, within_apply.compute
        )
        wrapped_within_apply = WithinApply(
            compute=[wrapped_compute],
            action=within_apply.action,
            source_ref=within_apply.source_ref,
        )
        self._builder.emit_statement(wrapped_within_apply)
