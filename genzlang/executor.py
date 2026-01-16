# executor.py
from .parser import parse
from .genzlang_core import process_line
from .conditionals import handle_condition_blocks
from .loops import handle_loop_block
from .functions import define_function

def run_program(lines):
    for item in parse(lines):
        if isinstance(item, list):
            # block
            header = item[0].strip()
            if header.startswith("spam"):
                handle_loop_block(item)
            elif header.startswith("vibe"):
                define_function(item)
            else:
                handle_condition_blocks(item)
        elif isinstance(item, str) and item.strip():
            process_line(item)
