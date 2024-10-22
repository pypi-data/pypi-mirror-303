from classiq.interface.generator.expressions.expression import Expression
from classiq.interface.generator.functions.builtins.internal_operators import (
    REPEAT_OPERATOR_NAME,
)
from classiq.interface.generator.functions.classical_type import Integer
from classiq.interface.model.classical_parameter_declaration import (
    ClassicalParameterDeclaration,
)
from classiq.interface.model.repeat import Repeat

from classiq.model_expansions.closure import FunctionClosure, GenerativeFunctionClosure
from classiq.model_expansions.quantum_operations.emitter import Emitter
from classiq.model_expansions.scope import Scope
from classiq.qmod.quantum_function import GenerativeQFunc


class RepeatEmitter(Emitter[Repeat]):
    def emit(self, repeat: Repeat, /) -> None:
        count = self._interpreter.evaluate(repeat.count).as_type(int)
        for i in range(count):
            with self._propagated_var_stack.capture_variables(repeat):
                self._emit_propagated(repeat, i)

    def _emit_propagated(self, repeat: Repeat, i: int) -> None:
        closure_constructor: type[FunctionClosure]
        extra_args: dict
        if repeat.is_generative():
            closure_constructor = GenerativeFunctionClosure
            extra_args = {
                "generative_blocks": {
                    "body": GenerativeQFunc(
                        repeat.get_generative_block("body"),
                    ),
                }
            }
        else:
            closure_constructor = FunctionClosure
            extra_args = {}
        iteration_function = closure_constructor.create(
            name=REPEAT_OPERATOR_NAME,
            positional_arg_declarations=[
                ClassicalParameterDeclaration(
                    name=repeat.iter_var, classical_type=Integer()
                )
            ],
            body=repeat.body,
            scope=Scope(parent=self._current_scope),
            **extra_args,
        )
        self._emit_quantum_function_call(iteration_function, [Expression(expr=str(i))])
