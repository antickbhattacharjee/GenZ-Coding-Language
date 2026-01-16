# __init__.py
# Initializes the GenZLang package

from .genzlang_core import process_line, variables, handle_lock, handle_yeet, handle_askin

__all__ = [
    "process_line",
    "variables",
    "handle_lock",
    "handle_yeet",
    "handle_askin",
]