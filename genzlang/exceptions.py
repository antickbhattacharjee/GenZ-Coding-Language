# exceptions.py
"""
Custom exception naming for GenZLang — map Python exceptions to GenZ names.
"""

EXCEPTION_MAP = {
    ZeroDivisionError: "NoDivideVibes",
    TypeError: "WrongTypeBruh",
    ValueError: "NahValue",
    NameError: "IDontKnowBro",
    IndexError: "OuttaBounds",
    KeyError: "NoKeyFr",
    AttributeError: "MissingVibe",
    SyntaxError: "NoSyntaxCap",
    FileNotFoundError: "FileGhosted",
    RuntimeError: "RuntimeSus",
    OverflowError: "BigBrainOverflow",
    ImportError: "ModuleMIA",
}


def get_genz_exception_name(exception):
    """Return the GenZ name for a given exception, or the default class name."""
    exc_type = type(exception)
    if exc_type in EXCEPTION_MAP:
        return EXCEPTION_MAP[exc_type]
    # fallback to Python exception class name
    return exc_type.__name__


def format_error_message(exception):
    """Format an exception as 'GenZName: message'."""
    genz_name = get_genz_exception_name(exception)
    return f"{genz_name}: {str(exception)}"
