import sys
from genzlang import process_line
from genzlang.executor import run_program
from genzlang.exceptions import format_error_message

if len(sys.argv) == 2:
    # run file (preserve original lines/indentation for block parsing)
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()
    try:
        run_program(lines)
    except Exception as e:
        # Print only the GenZ-formatted error, not the Python traceback
        print(f"Error: {format_error_message(e)}")
else:
    # REPL mode
    while True:
        code = input("GenZLang >>> ")
        if code.strip() == "exit":
            break
        process_line(code)
