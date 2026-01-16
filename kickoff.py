#!/usr/bin/env python3
"""Unified launcher: simple `kickoff filename.genz` usage.

Behavior:
- If called with no args: start the REPL (run run_genz.py with no file).
- If called with one arg that is a bare filename (e.g. `test_loop.genz` or `test_loop`),
  it will prefer `vibecode/<name>.genz` if present, otherwise treat the arg as a path
  relative to the repository root.
- Any additional args are forwarded to `run_genz.py`.
"""
from __future__ import annotations
import sys
from pathlib import Path
import subprocess


def main(argv: list[str]) -> int:
    repo = Path(__file__).resolve().parent

    if not argv:
        cmd = [sys.executable, str(repo / 'run_genz.py')]
        print('Starting REPL via run_genz.py')
        return subprocess.call(cmd)

    name = argv[0]
    extra = argv[1:]

    p = Path(name)
    # If no suffix, assume .genz
    if not p.suffix:
        p = p.with_suffix('.genz')

    # Prefer vibecode/<file> if it exists
    vibecode_candidate = (repo / 'vibecode' / p)
    repo_candidate = (repo / p)

    if vibecode_candidate.exists():
        target = vibecode_candidate
    elif repo_candidate.exists():
        target = repo_candidate
    else:
        # If user passed an absolute path or something that doesn't exist yet, still forward it
        # so run_genz.py can show a helpful error.
        if p.is_absolute():
            target = p
        else:
            # Try treating original string as a path relative to current working dir first
            cwd_candidate = Path.cwd() / p
            if cwd_candidate.exists():
                target = cwd_candidate
            else:
                # fallback to vibecode path (even if not existing) so behavior is predictable
                target = vibecode_candidate

    cmd = [sys.executable, str(repo / 'run_genz.py'), str(target)] + extra
    print('Running:', ' '.join(cmd))
    return subprocess.call(cmd)


if __name__ == '__main__':
    try:
        raise SystemExit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        print('\nInterrupted')
        raise SystemExit(1)
