import re

from classiq.interface.generator.compiler_keywords import CAPTURE_SUFFIX

IDENTIFIER_PATTERN = r"[a-zA-Z_][a-zA-Z0-9_]*"
CAPTURE_PATTERN = re.compile(
    rf"({IDENTIFIER_PATTERN}){CAPTURE_SUFFIX}{IDENTIFIER_PATTERN}__"
)


def mangle_captured_var_name(var_name: str, defining_function: str) -> str:
    return f"{var_name}{CAPTURE_SUFFIX}{defining_function}__"


def demangle_name(name: str) -> str:
    match = re.match(CAPTURE_PATTERN, name)
    return match.group(1) if match else name
