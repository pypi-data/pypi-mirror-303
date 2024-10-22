from typing import TYPE_CHECKING

from classiq.interface.model.quantum_function_call import QuantumFunctionCall

from classiq.model_expansions.call_to_model_converter import (
    BlockFunctionInfo,
    CallToModelConverter,
)
from classiq.model_expansions.closure import FunctionClosure
from classiq.model_expansions.quantum_operations.emitter import Emitter
from classiq.qmod.semantics.error_manager import ErrorManager

if TYPE_CHECKING:
    from classiq.model_expansions.interpreter import Interpreter


class QuantumFunctionCallEmitter(Emitter[QuantumFunctionCall]):
    def __init__(self, interpreter: "Interpreter") -> None:
        super().__init__(interpreter)
        self._model = self._interpreter._model
        self._synthesized_separately_blocks = (
            self._interpreter._synthesized_separately_blocks
        )

    def emit(self, call: QuantumFunctionCall, /) -> None:
        function: FunctionClosure = self._interpreter.evaluate(call.function).as_type(
            FunctionClosure
        )
        args = call.positional_args
        with ErrorManager().call(
            function.name
        ), function.scope.freeze(), self._propagated_var_stack.capture_variables(call):
            new_call = self._emit_quantum_function_call(function, args)
            if function.synthesis_data.should_synthesize_separately:
                interpreted_call_converter = CallToModelConverter(
                    call,
                    function.positional_arg_declarations,
                    function.scope.data,
                    self._model,
                )
                self._update_synthesized_separately_models(
                    interpreted_call_converter, new_call.func_name
                )

    def _update_synthesized_separately_models(
        self, call_converter: CallToModelConverter, call_name: str
    ) -> None:
        synthesized_separately_blocks = self._synthesized_separately_blocks
        block_id = call_converter.block_id
        block_function = synthesized_separately_blocks.get(block_id)
        if block_function is None:
            block_function = BlockFunctionInfo.from_call_converter(call_converter)
            synthesized_separately_blocks[block_id] = block_function
        block_function.calls.add(call_name)
