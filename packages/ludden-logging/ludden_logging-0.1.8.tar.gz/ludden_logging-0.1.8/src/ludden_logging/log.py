#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Efficient logger for the application with rich panel adjustments and fractional second display."""

from __future__ import annotations

from atexit import register
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import loguru
from dotenv import load_dotenv
from loguru import logger
from rich.console import Console
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)
from rich.style import Style
from rich.text import Text
from rich_gradient import Color, Gradient

from ludden_logging.run import Run, console

HOME: Path = Path.home()
CWD: Path = Path.cwd()
LOGS_DIR: Path = CWD / "logs"

load_dotenv()


class Log:
    """Efficient logger for the application with rich panel adjustments and fractional second display."""

    FORMAT: str = "{time:HH:mm:ss.SSS} | Run {extra[run]} | {file.name: ^12} | Line {line} | {level} | {message}"

    LEVEL_STYLES: Dict[str, Style] = {
        "TRACE": Style(italic=True),
        "DEBUG": Style(color="#aaaaaa"),
        "INFO": Style(color="#00afff"),
        "SUCCESS": Style(bold=True, color="#00ff00"),
        "WARNING": Style(italic=True, color="#ffaf00"),
        "ERROR": Style(bold=True, color="#ff5000"),
        "CRITICAL": Style(bold=True, color="#ff0000"),
    }

    GRADIENTS: Dict[str, Tuple[List[Color], bool, bool]] = {
        "TRACE": ([Color("#888888"), Color("#aaaaaa"), Color("#cccccc")], True, False),
        "DEBUG": ([Color("#338888"), Color("#55aaaa"), Color("#77cccc")], False, False),
        "INFO": ([Color("#008fff"), Color("#00afff"), Color("#00cfff")], True, False),
        "SUCCESS": (
            [Color("#00aa00"), Color("#00ff00"), Color("#afff00")],
            True,
            False,
        ),
        "WARNING": (
            [Color("#ffaa00"), Color("#ffcc00"), Color("#ffff00")],
            True,
            False,
        ),
        "ERROR": ([Color("#ff0000"), Color("#ff5500"), Color("#ff7700")], True, False),
        "CRITICAL": (
            [Color("#ff0000"), Color("#ff005f"), Color("#ff00af")],
            True,
            True,
        ),
    }
    progress = Progress(
        TextColumn("[progress.description]{task.description}"),
        SpinnerColumn(),
        BarColumn(bar_width=None),
        MofNCompleteColumn(),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
        console=console,
    )

    def __init__(
        self,
        user_run: Optional[int] = None,
        console: Console = console,
        log_to_console: int = 20,
        progress: bool = False,
    ) -> None:
        """Initialize logger and configure sinks.

        Args:
            run (Any): The Run object to get the current run count.
            console (Console, optional): The console object for logging. Defaults to console.
            log_to_console (int, optional): The log level to display in the console. Defaults to 20.
            progress (bool, optional): Whether to display a progress bar. Defaults to False.
        """
        self.console: Console = console
        self.console.line(9)
        self.console.clear()

        # Deal with Run object or run count
        if not user_run:
            run_instance = Run()
            run = run_instance.load()
            self.run = run
        else:
            self.run = user_run
        logger.remove()
        self.log_file = self.verify_log_file()

        # Initialize logging sinks only once
        logger.add(
            self.log_file,
            format=self.FORMAT,
            level="TRACE",
            backtrace=True,
            enqueue=True,
            colorize=True,
        )
        logger.add(
            self.rich_sink,
            format="{message}",
            level=log_to_console,
            backtrace=True,
            enqueue=True,
        )

        # Store extra information
        logger.configure(extra={"run": self.run})

    @property
    def run(self) -> int:
        """Get the current run count."""
        return self._run

    @run.setter
    def run(self, run: Optional[int] = None) -> None:
        """Set the current run count."""
        if run is None:
            if self.run is None:
                self._run: int = 0
            else:
                self._run = self.run
        else:
            self._run = run

    def increment(self) -> int:
        """Increment the run count."""
        self.run = self.run + 1
        return self.run

    def verify_logs_dir(self) -> Path:
        """Verify the existence of the logs directory.

        Returns:
            the logs directory path.
        """
        CWD = Path.cwd()
        LOGS_DIR = CWD / "logs"
        if not LOGS_DIR.exists():
            LOGS_DIR.mkdir(parents=True)
        return LOGS_DIR

    def verify_log_file(self) -> Path:
        """Get the log file path."""
        LOGS_DIR = self.verify_logs_dir()
        log_file = LOGS_DIR / "trace.log"
        return log_file

    def log(self, level: str | int, message: Any) -> None:
        """Log a message.

        Args:
            level (str): The logging level.
            message (Any): The object(s) to log.
        """
        if Path(__file__).parent.name == "ludden_logging":
            depth = 1
        else:
            depth = 2
        if isinstance(level, int):
            logger.opt(depth=depth).log(
                level,
                message,
            )
        else:
            logger.opt(depth=depth).log(level.upper(), message)

    def trace(self, message: Any) -> None:
        """Log a message with level 'TRACE'.

        Args:
            message (Any): The object(s) to log.

        Example:
            >>> log.trace("Trace message.")
        """
        logger.trace(message)

    def debug(self, message: Any) -> None:
        """Log a message with the level 'DEBUG'.

        Args:
            message (Any): The object(s) to log.

        Example:
            >>> log.debug("Debug message.")
        """
        logger.debug(message)

    def info(self, message: Any) -> None:
        """Log a message with the level 'INFO'.

        Args:
            message (Any): The object(s) to log.

        Example:
            >>> log.info("Info message.")
        """
        logger.info(message)

    def success(self, message: Any) -> None:
        """Log a message with the level 'SUCCESS'.

        Args:
            message (Any): The object(s) to log.

        Example:
            >>> log.success("Success message.")
        """
        logger.success(message)

    def warning(self, message: Any) -> None:
        """Log a message with the level 'WARNING'.

        Args:
            message (Any): The object(s) to log.

        Example:
            >>> log.warning("Warning message.")
        """
        logger.warning(message)

    def error(self, message: Any) -> None:
        """Log an message with the level 'ERROR'.

        Args:
            message (Any): The object(s) to log.

        Example:
            >>> log.error("Error message.")
        """
        logger.error(message)

    def critical(self, message: Any) -> None:
        """Log a message with the level 'CRITICAL'.

        Args:
            message (Any): The object(s) to log.

        Example:
            >>> log.critical("Critical message.")
        """
        logger.critical(message)

    def rich_sink(self, message: Any) -> None:
        """Custom Rich sink to log styled messages to the console."""
        record: loguru.Record = message.record
        level: str = record["level"].name
        style: Style = self.LEVEL_STYLES.get(level, Style())

        colors, bold, italic = self.GRADIENTS.get(level, ([], False, False))

        # Title includes log level and file/line info
        title: Text = Gradient(
            f" {level} | {record['file'].name} | Line {record['line']} ", colors
        ).as_text()
        title.highlight_words("|", style="italic #666666")
        title.stylize(Style(reverse=True))

        # Subtitle includes run count and time with fractional seconds (milliseconds)
        subtitle: Text = Text.assemble(
            Text(f"Run {self.run} | "),
            Text(record["time"].strftime("%H:%M:%S.%f")[:-3]),
            Text(record["time"].strftime(" %p")),
        )
        subtitle.highlight_words(":", style="dim #aaaaaa")

        # Message text
        message_text: Text = Gradient(record["message"], colors, style="bold")

        # Generate and print log panel with aligned title and subtitle
        log_panel: Panel = Panel(
            message_text,
            title=title,
            title_align="left",  # Left align the title
            subtitle=subtitle,
            subtitle_align="right",  # Right align the subtitle
            border_style=style + Style(bold=True),
            padding=(1, 2),
        )
        self.console.print(log_panel)

    def opt(
        self,
        *,
        exception: Optional[bool | Tuple | Exception] = None,
        record: bool = False,
        lazy: bool = False,
        colors: bool = False,
        raw: bool = False,
        capture: bool = True,
        depth: int = 0,
        ansi: int = False,
    ) -> loguru.Logger:
        """Set options for the logger.

        Args:
            exception (bool, tuple, Exception, optional):
                If It Does Not Evaluate As ``False``, The Passed Exception Is Formatted And Added To The
                Log Message. It Could Be An |Exception| Object Or A ``(Type, Value, Traceback)`` Tuple,
                Otherwise The Exception Information Is Retrieved From |Sys.Exc_info|. Defaults to None.
            record (bool, optional):
                If ``True``, The Record Dict Contextualizing The Logging Call Can Be Used To Format The
                Message By Using ``{Record[Key]}`` In The Log Message. Defaults to False.
            lazy (bool, optional):
                If ``True``, The Logging Call Attribute To Format The Message Should Be Functions Which
                Will Be Called Only If The Level Is High Enough. This Can Be Used To Avoid Expensive
                Functions If Not Necessary. Defaults to False.
            colors (bool, optional):
                If ``True``, Logged Message Will Be Colorized According To The Markups It Possibly
                Contains. Defaults to False.
            raw (bool, optional):
                If ``True``, The Formatting Of Each Sink Will Be Bypassed And The Message Will Be Sent
                As Is. Defaults to False.
            capture (bool, optional):
                If ``False``, The ``**Kwargs`` Of Logged Message Will Not Automatically Populate
                The ``Extra`` Dict (Although They Are Still Used For Formatting). Defaults to True.
            depth (int, optional):
                Specify Which Stacktrace Should Be Used To Contextualize The Logged Message. This Is
                Useful While Using The Logger From Inside A Wrapped Function To Retrieve Worthwhile
                Information. Defaults to 0.
            ansi (int, optional):
                Deprecated Since Version 0.4.1: The ``Ansi`` Parameter Will Be Removed In Loguru 1.0.0,
                It Is Replaced By ``Colors`` Which Is A More Appropriate Name. Defaults to False.
        """
        return logger.opt(
            exception=exception,  # type: ignore
            record=record,
            lazy=lazy,
            colors=colors,
            raw=raw,
            capture=capture,
            depth=depth,
            ansi=ansi,  # type: ignore
        )


register(Log().increment)  # type: ignore

if __name__ == "__main__":
    from ludden_logging.run import Run  # Assuming Run is defined in run.py

    log = Log()
    log.increment()

    # Log test messages
    log.log("TRACE", "Trace message.")
    log.log("DEBUG", "Debug message.")
    log.log("INFO", "Info message.")
    log.log("SUCCESS", "Success message.")
    log.log("WARNING", "Warning message.")
    log.log("ERROR", "Error message.")
    log.log("CRITICAL", "Critical message.")
