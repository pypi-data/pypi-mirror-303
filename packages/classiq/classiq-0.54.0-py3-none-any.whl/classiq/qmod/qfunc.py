from typing import Callable, Literal, Optional, Union, overload

from classiq.qmod.quantum_callable import QCallable
from classiq.qmod.quantum_function import ExternalQFunc, GenerativeQFunc, QFunc

GEN_QFUNCS: list[GenerativeQFunc] = []
DEC_QFUNCS: list[QFunc] = []


def set_discovered_functions(
    dec_funcs: list[QFunc], gen_funcs: list[GenerativeQFunc]
) -> None:
    DEC_QFUNCS.clear()
    DEC_QFUNCS.extend(dec_funcs)
    GEN_QFUNCS.clear()
    GEN_QFUNCS.extend(gen_funcs)


@overload
def qfunc(func: Callable) -> QFunc: ...


@overload
def qfunc(*, external: Literal[True]) -> Callable[[Callable], ExternalQFunc]: ...


@overload
def qfunc(*, generative: Literal[True]) -> Callable[[Callable], GenerativeQFunc]: ...


def qfunc(
    func: Optional[Callable] = None, *, external: bool = False, generative: bool = False
) -> Union[Callable[[Callable], QCallable], QCallable]:
    def wrapper(func: Callable) -> QCallable:
        if generative:
            gen_qfunc = GenerativeQFunc(func)
            GEN_QFUNCS.append(gen_qfunc)
            return gen_qfunc
        if external:
            return ExternalQFunc(func)
        dec_qfunc = QFunc(func)
        DEC_QFUNCS.append(dec_qfunc)
        return dec_qfunc

    if func is not None:
        return wrapper(func)

    return wrapper
