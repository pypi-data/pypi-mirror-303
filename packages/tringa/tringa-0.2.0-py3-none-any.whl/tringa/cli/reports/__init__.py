from typing import Protocol

from rich.console import Console, ConsoleOptions, RenderResult


class Report(Protocol):
    def summary(self) -> "Report":
        return self

    def to_dict(self) -> dict: ...

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...
