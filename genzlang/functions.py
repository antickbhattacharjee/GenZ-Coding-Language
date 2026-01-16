# functions.py
"""
Simple function support for GenZLang.

Syntax supported:

vibe fname(arg1, arg2):
    <body lines indented>
endvibe

Call syntax:
spit fname(1, 2)

This module stores function definitions in a global dict `functions`.
Each function is a dict with keys: 'name', 'args' (list), 'body' (list of lines).

Function calls are executed by the `call_function` helper which evaluates
arguments in the current `variables` context, sets up a local frame by
pushing and popping variables in the shared `variables` dict.

Note: This is deliberately simple—no closures, no recursion guards, and
arguments are passed by value (evaluated) into the function's parameter names.
"""
from . import genzlang_core
import re

functions = {}

ARG_LIST_RE = re.compile(r"\s*([a-zA-Z_]\w*)\s*(?:,\s*([a-zA-Z_]\w*)\s*)*")


def parse_vibe_header(header: str):
    """Parse a `vibe name(arg,...)` header and return (name, [args]) or None."""
    header = header.strip().rstrip(":")
    if not header.startswith("vibe "):
        return None
    rest = header[len("vibe "):].strip()
    # expect: name(arg1, arg2)
    m = re.match(r"([a-zA-Z_]\w*)\s*\((.*)\)", rest)
    if not m:
        return None
    name = m.group(1)
    args_str = m.group(2).strip()
    if not args_str:
        args = []
    else:
        args = [a.strip() for a in args_str.split(",")]
    return name, args


def define_function(block_lines):
    """Register a function from a block: header + indented body."""
    header = block_lines[0].strip()
    parsed = parse_vibe_header(header)
    if not parsed:
        print(f"Error: invalid vibe header: {header}")
        return
    name, args = parsed
    body = [ln.lstrip() for ln in block_lines[1:]]
    functions[name] = {"name": name, "args": args, "body": body}


def call_function(name: str, arg_values):
    """Call a previously defined function.

    - `arg_values` is a list of already-evaluated Python objects.
    - Sets parameters in `variables`, runs the body, and returns the value
      of a special variable `__return__` if set (else None).
    """
    if name not in functions:
        raise NameError(f"function '{name}' is not defined")
    fn = functions[name]
    params = fn["args"]

    # Simple arity check
    if len(params) != len(arg_values):
        raise TypeError(f"{name}() takes {len(params)} positional arguments but {len(arg_values)} were given")

    # Save old values to restore after call (operate on genzlang_core.variables)
    vars_dict = genzlang_core.variables
    saved = {p: vars_dict.get(p, None) for p in params}
    # Set parameters
    for p, v in zip(params, arg_values):
        vars_dict[p] = v

    # Clear any previous __return__
    prev_return = vars_dict.pop("__return__", None)

    # Execute body lines
    for line in fn["body"]:
        genzlang_core.process_line(line)

    # Grab return value if set
    ret = vars_dict.pop("__return__", None)

    # Restore saved params
    for p, v in saved.items():
        if v is None:
            vars_dict.pop(p, None)
        else:
            vars_dict[p] = v

    # Restore previous __return__ (rarely used)
    if prev_return is not None:
        vars_dict["__return__"] = prev_return

    return ret


# Optional helper: allow `spit fn(a,b)` to route here from genzlang_core
def try_call_by_name(call_expr: str):
    """Try to interpret `name(expr,...)` and call if it's a known vibe.
    Returns (called, value_or_error)
    """
    call_expr = call_expr.strip()
    m = re.match(r"([a-zA-Z_]\w*)\s*\((.*)\)", call_expr)
    if not m:
        return False, None
    name = m.group(1)
    args_str = m.group(2).strip()
    if name not in functions:
        return False, None
    # parse arguments by splitting on commas (simple)
    if not args_str:
        arg_texts = []
    else:
        # naive split — assumes no nested commas
        arg_texts = [a.strip() for a in args_str.split(",")]
    try:
        arg_values = [eval(a, {}, genzlang_core.variables) for a in arg_texts]
    except Exception as e:
        return True, e
    try:
        res = call_function(name, arg_values)
    except Exception as e:
        return True, e
    return True, res
