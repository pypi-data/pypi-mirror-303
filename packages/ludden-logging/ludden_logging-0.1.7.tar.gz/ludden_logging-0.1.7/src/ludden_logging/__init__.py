
from rich.console import Console
from rich.traceback import install as tr_install
# from atexit import register

from ludden_logging.run import Run
from ludden_logging.log import Log

__all__ = [
    "Log",
    "Run"
]

console = Console()
tr_install(console=console)
run = Run().load()
log = Log(run)

