from typing import Any, List, Optional

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

class Writer:
    def __init__(self, **kwargs) -> None:
        self.console_kwargs = {"width": 80}
        self.console_kwargs.update(kwargs)

    def writer(self, string: str, *args, **kwargs) -> None:
        console = Console(**self.console_kwargs)
        console.print(string, *args, **kwargs)

    def __call__(self, string: str, *args, **kwargs) -> None:
        self.writer(string, *args, **kwargs)

    def write_header(self, string: str) -> None:
        console = Console(**self.console_kwargs)
        console.rule(string)

    def write_table(self, table_columns: List, table_rows: List, **table_kwargs) -> None:
        console = Console(**self.console_kwargs)

        table = Table(**table_kwargs)
        for column in table_columns:
            table.add_column(column)

        for row in table_rows:
            table.add_row(*row)

        console.print(table)

    def write_panel(self, panel_content: str, panel_title: Optional[str] = None) -> None:
        console = Console(**self.console_kwargs)
        panel = Panel(panel_content, title=panel_title)
        console.print(panel)