#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Get the current working directory as a Path object."""
from os import getenv
from pathlib import Path
from typing import Optional

from ludden_logging import console


def cwd(path: Optional[Path] = None, verbose: bool = False) -> Path:
    """Get the current working directory as a Path object."""
    console.clear()
    console.line(2)
    venv = getenv("VIRTUAL_ENV_PROMPT")
    cwd = Path.cwd()
    if verbose:
        console.log(f"Current virtual environment: {venv}")
        console.log(f"Current working directory: {cwd}")
        console.line(2)
    if not venv:
        console.log("No virtual environment detected.")
        raise EnvironmentError("No virtual environment detected.")
    else:
        if venv == cwd.parent.stem:
            if verbose:
                console.log("The virtual environment matches the parent directory.")
            return cwd
        else:
            return Path.home() / "dev" / "py" / venv


if __name__ == '__main__':
    cwd(verbose=True)
