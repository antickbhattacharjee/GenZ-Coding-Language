# loops.py
from .genzlang_core import process_line, variables
import re

def parse_loop_header(line: str):
    """Parse spam loops and return loop info dict."""
    line = line.strip().rstrip(":")
    if not line.startswith("spam "):
        return None
    tokens = line.split()

    # infinite loop
    if "always" in tokens:
        return {"type": "infinite"}

    # while-like condition: check the part after 'spam '
    rest = line[len("spam "):].strip()
    if re.search(r"[<>=!]", rest):
        return {"type": "while", "condition": rest}

    # need at least a loop var
    if len(tokens) < 2:
        return None

    var = tokens[1]
    loop_info = {"type": "range", "var": var, "start": 0, "end": None, "step": 1}

    # til loop: 'spam i til 10'
    if "til" in tokens:
        try:
            loop_info["end"] = int(tokens[tokens.index("til") + 1])
        except (IndexError, ValueError):
            print(f"Error: invalid 'til' value in loop header: {line}")
            return None
        loop_info["start"] = variables.get(var, 0)
        loop_info["step"] = 1 if loop_info["end"] >= loop_info["start"] else -1
        return loop_info

    # from ... to ... loop: 'spam i from 0 to 10 [drip 2]'
    if "from" in tokens and "to" in tokens:
        try:
            start = int(tokens[tokens.index("from") + 1])
            end = int(tokens[tokens.index("to") + 1])
        except (IndexError, ValueError):
            print(f"Error: invalid 'from'/'to' values in loop header: {line}")
            return None
        loop_info["start"] = start
        loop_info["end"] = end

        if "drip" in tokens:
            try:
                loop_info["step"] = int(tokens[tokens.index("drip") + 1])
            except (IndexError, ValueError):
                print(f"Error: invalid 'drip' value in loop header: {line}")
                return None
        else:
            loop_info["step"] = 1 if end >= start else -1

        return loop_info

    # shorthand: 'spam i 10' treat tokens[2] as end
    if len(tokens) >= 3:
        try:
            loop_info["end"] = int(tokens[2])
            loop_info["start"] = variables.get(var, 0)
            loop_info["step"] = 1 if loop_info["end"] >= loop_info["start"] else -1
            return loop_info
        except ValueError:
            pass

    return None

def handle_loop_block(block_lines):
    """Execute a spam block."""
    header = block_lines[0].strip()
    body = [ln.lstrip() for ln in block_lines[1:]]
    loop_info = parse_loop_header(header)

    if not loop_info:
        print(f"Error: Invalid loop header: {header}")
        return

    # infinite loop
    if loop_info["type"] == "infinite":
        while True:
            for stmt in body:
                if stmt.strip() == "nospam":
                    return
                process_line(stmt)
        return

    # while-like loop
    if loop_info["type"] == "while":
        while eval(loop_info["condition"], {}, variables):
            for stmt in body:
                if stmt.strip() == "nospam":
                    return
                process_line(stmt)
        return

    # range loop
    if loop_info["type"] == "range":
        var = loop_info["var"]
        start = loop_info["start"]
        end = loop_info["end"]
        step = loop_info["step"]

        current = start
        variables[var] = current  # ensure loop var exists globally
        cond_fn = (lambda v: v <= end) if step > 0 else (lambda v: v >= end)

        while cond_fn(current):
            variables[var] = current
            for stmt in body:
                if stmt.strip() == "nospam":
                    return
                process_line(stmt)
            current += step
