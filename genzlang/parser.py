# parser.py
from .conditionals import handle_condition_blocks
from .loops import handle_loop_block

def is_block_start(line: str) -> bool:
    line = line.strip()
    return (
        line.startswith("nocap") or
        line.startswith("deadass") or
        line.startswith("cap") or
        line.startswith("spam") or
        line.startswith("vibe") or
        line.startswith("tryhard")
    ) and line.endswith(":")

def collect_block(lines, start_index):
    """Collect indented lines for a block."""
    block = [lines[start_index]]
    i = start_index + 1
    while i < len(lines) and (lines[i].startswith(" ") or lines[i].startswith("\t")):
        block.append(lines[i])
        i += 1
    return block, i

def parse(lines):
    """
    Yields either:
      - single-line instructions
      - full blocks (list of lines)
    """
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if is_block_start(line):
            block, i = collect_block(lines, i)
            yield block  # yield the whole block
            continue

        yield line
        i += 1
