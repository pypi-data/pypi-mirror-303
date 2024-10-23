#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Track the number of runs of a module, stored in both a file and an environment variable."""
import os
from pathlib import Path
from typing import Optional

from rich.console import Console
from rich.prompt import IntPrompt
from rich.traceback import install as tr_install


# from ludden_logging import console

console = Console(
    # style=Style(color="#ffffff", bgcolor="#30173d", bold=True),
    # width=120,
)

tr_install(console=console)


class Run:
    """Class to track the number of runs of a module, stored in both a file and an environment variable."""

    white = "#ffffff"
    radiate = "#d7ff64"
    space = "#30173d"
    tab = "\t\t"

    def __init__(
        self,
        run: Optional[int] = None,
        project_name: Optional[str] = None,
        run_file: Optional[Path] = None,
        console: Console = console,
        verbose: bool = False,
    ) -> None:
        """Initialize the Run class and load the run count.

        Args:
            project_name (Optional[str], optional): The name of the project for setting up the environment variable.
            run_file (Optional[Path], optional): The file where the run count is stored. Defaults to 'logs/run.txt'.
        """
        # Set the project name
        self.project_name = project_name or self.get_project_name()

        # Set the verbose flag
        self.verbose: bool = verbose
        if verbose:
            # Print the project name
            console.line()
            console.print(
                f"[b on {self.space}][#ffffff]Project name:[/#ffffff] \
[{self.radiate}]{self.project_name}[/{self.radiate}]"
            )

        # Set the environment variable name
        self.env_var_name = f"{self.project_name.upper()}_RUN_COUNT"

        # Default log file location
        self.run_file = run_file or Path.cwd() / "logs" / "run.txt"
        self.run_file.parent.mkdir(
            parents=True, exist_ok=True
        )  # Ensure the log directory exists

        self.run = run or self.load()

    @property
    def run(self) -> int:
        """Get the current run count from the environment variable."""
        return self._run

    @run.setter
    def run(self, value: Optional[int]) -> None:
        """Set the run count in the environment variable."""
        if value is None:  # Check explicitly for None to avoid blocking valid values like 0
            value = IntPrompt.ask(
                f"[{self.space}][#ffffff]Enter the run \
count for '[{self.radiate}]{self.project_name}[/{self.radiate}]"
            )
            assert isinstance(value, int), "Run count must be an integer."
            assert value > 0, "Run count must be greater than 0."
            self._run = value
        else:
            self._run = value

    def __add__(self, other: int) -> int:
        """Add the run count to another integer."""
        if isinstance(other, int):
            return self.run + other
        raise TypeError("Can only add integers to the run count")

    def load(self, user_run: Optional[int] = None) -> int:
        """Load the current run count from the run file and set it to an environment variable.

        Returns:
            int: The current run count.
        """
        if user_run is not None:
            return user_run
        if self.run_file.exists():
            try:
                # Load from the file
                with open(self.run_file, "r", encoding="utf-8") as file:
                    run_count = int(file.read().strip())
            except ValueError:  # Removed redundant FileNotFoundError
                run_count = 0
        else:
            # File doesn't exist, initialize it and notify the user
            run_count = 0
            console.print(
                f"[{self.space}][i white]Run file '[/i white][b {self.radiate}]{self.run_file}[/b \
{self.radiate}][i white]' does not exist. Creating it with an initial count of [/i white]\
[b {self.radiate}]0[/b {self.radiate}]."
            )
            self.save(run_count)

        # Set the run count in the environment variable
        os.environ[self.env_var_name] = str(run_count)

        return run_count

    def increment(self) -> None:
        """Increment the run count, save it to both the run file and the environment variable."""
        self.run = self.run + 1
        self.save(self.run)

    def reset(self) -> None:
        """Reset the run count to 0 and save it to both the run file and the environment variable."""
        self.run = 0
        self.save(self.run)

    def save(self, run_count: int) -> None:
        """Save the run count to the run file and set it in the environment variable.

        Args:
            run_count (int): The run count to be saved.
        """
        # Save to the file
        try:
            with open(self.run_file, "w", encoding="utf-8") as file:
                file.write(str(run_count))
        except PermissionError as e:
            console.print(f"[on red]PermissionError: {e}[/]")

        # Set the run count in the environment variable
        os.environ[self.env_var_name] = str(run_count)
        if self.verbose:
            console.print(
                f"[on {self.space}][white]Run count updated to [b {self.radiate}]{run_count}\
[/b {self.radiate}]. Stored in:\n\t- [b {self.radiate}]{self.run_file}[/b {self.radiate}] and\n\t- \
environment variable [b {self.radiate}]{self.env_var_name}[/b {self.radiate}]."
            )

    @classmethod
    def get_project_name(cls) -> str:
        """Get the project name from the pyproject.toml file."""
        try:
            with open("pyproject.toml", "r", encoding="utf-8") as file:
                for line in file:
                    if "name" in line:
                        return line.split(" = ")[1].strip().strip('"')
        except FileNotFoundError:
            console.print(
                f"[on {cls.space}][b][#ffffff]No '[/white][{cls.radiate}][{cls.radiate}]pyproject.toml\
[/{cls.radiate}][#ffffff]' file found. Using `default` as name."
            )
            return "default"

        return Path(__file__).parent.name


# Example usage:
if __name__ == "__main__":
    track = Run(verbose=True)

    console.print(
        f"[on {track.space}][b][#ffffff]Current run count: \
[/#ffffff][{track.radiate}]{track.run}[/{track.radiate}][#ffffff]"
    )

    # Increment the run count
    track.increment()

    # The run count is now also available in the environment
    console.print(
        f"[on {track.space}][b][#ffffff]Environment variable \
'[/#ffffff][{track.radiate}]{track.env_var_name}[/{track.radiate}]\
[#ffffff]': [/#ffffff][{track.radiate}]{os.getenv(track.env_var_name)}\
[/{track.radiate}]"
    )
