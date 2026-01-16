# genzlang_core.py
# Module to handle variable declaration, input, and output for GenZLang

# Storage for variables
from .builtins import GENZLANG_BUILTINS

variables = GENZLANG_BUILTINS.copy()


def handle_lock(statement):
    """
    Handles variable declaration: lock var = value
    """
    try:
        _, rest = statement.split("lock", 1)
        var, value = rest.split("=", 1)
        var = var.strip()
        # use variables as globals
        variables[var] = eval(value.strip(), variables)
    except Exception as e:
        from .exceptions import format_error_message
        print(f"Error in lock statement: {format_error_message(e)}")


def handle_yeet(statement):
    """
    Handles output: yeet(value)
    """
    try:
        inside = statement.strip()[5:-1]  # extract inside yeet(...)
        # allow function calls defined via `vibe` to be used here
        from .functions import try_call_by_name

        called, result = try_call_by_name(inside)
        if called:
            if isinstance(result, Exception):
                raise result
            print(result)
            return

        value = eval(inside, variables)    # use variables as globals
        print(value)
    except Exception as e:
        from .exceptions import format_error_message
        print(f"Error in yeet: {format_error_message(e)}")
        raise


def handle_askin(statement):
    """
    Handles input: askin("text")
    Returns string
    """
    try:
        inside = statement.strip()[6:-1]
        # use variables as globals for evaluating prompt
        prompt = eval(inside, variables)
        return input(prompt + " ")
    except Exception as e:
        from .exceptions import format_error_message
        print(f"Error in askin: {format_error_message(e)}")
        return ""


def process_line(line):
    """
    Processes a single GenZLang line.
    """
    line = line.strip()

    if line.startswith("lock"):
        # variable assignment with possible askin
        if "askin(" in line:
            var = line.split("lock", 1)[1].split("=")[0].strip()
            prompt_part = line.split("=", 1)[1].strip()
            variables[var] = handle_askin(prompt_part)
        else:
            handle_lock(line)

    elif line.startswith("yeet"):
        handle_yeet(line)

    elif line.startswith("spit"):
        # set a special return variable for functions
        try:
            # support both `spit expr` and `spit(expr)`
            inside = line[4:].strip()
            if inside.startswith("(") and inside.endswith(")"):
                inside = inside[1:-1]

            # allow function calls via try_call_by_name
            from .functions import try_call_by_name
            called, result = try_call_by_name(inside)
            if called:
                if isinstance(result, Exception):
                    raise result
                variables["__return__"] = result
            else:
                variables["__return__"] = eval(inside, variables)
        except Exception as e:
            from .exceptions import format_error_message
            print(f"Error in spit: {format_error_message(e)}")

    elif line.startswith("askin"):
        # standalone input
        return handle_askin(line)

    # Try bare function call like `fname(args)` as a statement
    try:
        from .functions import try_call_by_name
        called, result = try_call_by_name(line)
        if called:
            if isinstance(result, Exception):
                print(f"Error in call: {result}")
            # if result is not None, we don't automatically yeet it here —
            # function bodies can `yeet` themselves or callers can wrap in `yeet(...)`.
            return
    except Exception:
        # keep original behavior on any import/eval error
        pass
