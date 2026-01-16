# conditionals.py
# Handles GenZLang conditional statements: nocap, deadass, cap

from .genzlang_core import variables, process_line

def evaluate_condition(expr: str) -> bool:
    """Evaluate a GenZLang condition using Python eval with GenZ operators."""
    try:
        # Replace GenZ operators with Python ones
        expr = expr.replace("samevibe", "==")
        expr = expr.replace("diffvibe", "!=")
        expr = expr.replace("andfr", "and")
        expr = expr.replace("orwhateva", "or")
        expr = expr.replace("nah", "not ")
        # Eval with variables as both globals and locals to ensure visibility
        return bool(eval(expr, variables, variables))
    except Exception as e:
        print(f"Condition error: {e}")
        return False


def execute_block(block_lines):
    """Execute the lines inside a conditional block."""
    for line in block_lines:
        process_line(line)


def handle_condition_blocks(lines):
    """
    Process a list of lines containing nocap, deadass, and cap blocks.
    Preserves indentation for nested blocks.
    """

    i = 0
    executed = False

    while i < len(lines):
        line = lines[i].rstrip()

        # IF block
        if line.startswith("nocap") and line.endswith(":"):
            cond = line[5:-1].strip().strip("()")
            block = []
            i += 1

            # collect indented block (keep indentation)
            while i < len(lines) and (lines[i].startswith(" ") or lines[i].startswith("\t")):
                block.append(lines[i])
                i += 1

            if evaluate_condition(cond) and not executed:
                execute_block(block)
                executed = True
            continue

        # ELIF block
        if line.startswith("deadass") and line.endswith(":"):
            cond = line[8:-1].strip().strip("()")
            block = []
            i += 1

            while i < len(lines) and (lines[i].startswith(" ") or lines[i].startswith("\t")):
                block.append(lines[i])
                i += 1

            if evaluate_condition(cond) and not executed:
                execute_block(block)
                executed = True
            continue

        # ELSE block
        if line.startswith("cap") and line.endswith(":"):
            block = []
            i += 1

            while i < len(lines) and (lines[i].startswith(" ") or lines[i].startswith("\t")):
                block.append(lines[i])
                i += 1

            if not executed:
                execute_block(block)
            continue

        # TRY/EXCEPT/FINALLY block (tryhard)
        if line.startswith("tryhard") and line.endswith(":"):
            # collect inline rest of header and indented block lines
            # header may contain inline clauses: "tryhard: <try> sus err: <except> frfr: <finally>"
            raw = line
            # get the part after the first ':' (may be empty)
            try:
                rest = raw.split(":", 1)[1].strip()
            except Exception:
                rest = ""

            block = []
            i += 1
            while i < len(lines) and (lines[i].startswith(" ") or lines[i].startswith("\t")):
                block.append(lines[i].lstrip())
                i += 1

            # Combine inline rest and indented block into a single text to parse clauses
            combined = rest
            if block:
                if combined:
                    combined += " ; " + " ; ".join(b.rstrip() for b in block)
                else:
                    combined = " ; ".join(b.rstrip() for b in block)

            # Find clause markers
            err_marker = " sus err:"
            finally_marker = " frfr:"
            pos_err = combined.find(err_marker) if combined else -1
            pos_fin = combined.find(finally_marker) if combined else -1

            try_text = ""
            err_text = ""
            fin_text = ""

            if combined:
                if pos_err == -1 and pos_fin == -1:
                    try_text = combined
                elif pos_err != -1 and (pos_fin == -1 or pos_err < pos_fin):
                    try_text = combined[:pos_err].strip()
                    if pos_fin != -1:
                        err_text = combined[pos_err + len(err_marker):pos_fin].strip()
                        fin_text = combined[pos_fin + len(finally_marker):].strip()
                    else:
                        err_text = combined[pos_err + len(err_marker):].strip()
                elif pos_fin != -1 and (pos_err == -1 or pos_fin < pos_err):
                    try_text = combined[:pos_fin].strip()
                    fin_text = combined[pos_fin + len(finally_marker):].strip()

            # Helper to split inline segment into statements
            def split_stmts(text):
                if not text:
                    return []
                # prefer semicolon as separator; fall back to single statement
                if ";" in text:
                    return [s.strip() for s in text.split(";") if s.strip()]
                # otherwise treat as single statement (may already contain multiple statements separated by spaces)
                return [text.strip()]

            try_stmts = split_stmts(try_text)
            err_stmts = split_stmts(err_text)
            fin_stmts = split_stmts(fin_text)

            # Execute try/except/finally
            try:
                if try_stmts:
                    for stmt in try_stmts:
                        process_line(stmt)
                else:
                    # nothing in inline try — no-op
                    pass
            except Exception as e:
                if err_stmts:
                    for stmt in err_stmts:
                        process_line(stmt)
                else:
                    # default behavior: print the exception with GenZ name
                    from .exceptions import format_error_message
                    print(f"Error in tryhard: {format_error_message(e)}")
            finally:
                if fin_stmts:
                    for stmt in fin_stmts:
                        process_line(stmt)
            continue

        i += 1
