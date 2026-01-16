# builtins.py
"""
GenZLang built-in functions and type conversions.
"""

def textvibe(value):
    """Convert to string."""
    return str(value)


def numbruh(value):
    """Convert to integer."""
    return int(value)


def decimaldrip(value):
    """Convert to float."""
    return float(value)


def truetrip(value):
    """Convert to boolean."""
    return bool(value)


def squad(value):
    """Convert to list."""
    return list(value)


def mapfr(value):
    """Convert to dict."""
    if isinstance(value, dict):
        return value
    # if it's an iterable of pairs, try to construct a dict
    return dict(value)


def nahbruh():
    """Return None."""
    return None


def askintextvibe(prompt):
    """Input as string (same as askin but with GenZ name)."""
    return input(prompt + " ")


def askinnumbruh(prompt):
    """Input as integer."""
    return int(input(prompt + " "))


def askindeckydrip(prompt):
    """Input as float."""
    return float(input(prompt + " "))


# Export all builtins
GENZLANG_BUILTINS = {
    "textvibe": textvibe,
    "numbruh": numbruh,
    "decimaldrip": decimaldrip,
    "truetrip": truetrip,
    "squad": squad,
    "mapfr": mapfr,
    "nahbruh": nahbruh,
    "askintextvibe": askintextvibe,
    "askinnumbruh": askinnumbruh,
    "askindeckydrip": askindeckydrip,
    # Also keep standard Python conversions for compatibility
    "int": int,
    "str": str,
    "float": float,
    "bool": bool,
    "list": list,
    "dict": dict,
}
