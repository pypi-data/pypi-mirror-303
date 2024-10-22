from classiq.interface.generator.functions.builtins.internal_operators import (
    INVERT_OPERATOR_NAME,
)
from classiq.interface.model.invert import Invert

from classiq.model_expansions.closure import Closure
from classiq.model_expansions.quantum_operations.emitter import Emitter
from classiq.model_expansions.scope import Scope


class InvertEmitter(Emitter[Invert]):
    def emit(self, invert: Invert, /) -> None:
        with self._propagated_var_stack.capture_variables(invert):
            self._emit_propagated(invert)

    def _emit_propagated(self, invert: Invert, /) -> None:
        if invert.is_generative():
            context = self._register_generative_context(invert, INVERT_OPERATOR_NAME)
            invert = invert.model_copy(update={"body": context.statements("body")})

        if self._should_wrap(invert.body):
            self._emit_wrapped(invert)
            return

        self._emit_as_operation(invert)

    def _emit_as_operation(self, invert: Invert) -> None:
        invert_operation = Closure(
            name=INVERT_OPERATOR_NAME,
            blocks={"body": invert.body},
            scope=Scope(parent=self._current_scope),
        )
        context = self._expand_operation(invert_operation)
        self._builder.emit_statement(
            Invert(body=context.statements("body"), source_ref=invert.source_ref)
        )

    def _emit_wrapped(self, invert: Invert) -> None:
        wrapping_function = self._create_expanded_wrapping_function(
            INVERT_OPERATOR_NAME, invert.body
        )
        self._builder.emit_statement(
            Invert(body=[wrapping_function], source_ref=invert.source_ref)
        )
