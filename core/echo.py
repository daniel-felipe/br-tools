from rich.console import Console
from rich.table import Table


class Echo:
    def __init__(self):
        self._console = Console()
        self._table = Table()

    def print(self, content):
        self._console.print(f'[[green]+[/green]] {content}')

    def error(self, content):
        self._console.print(f'[[red]-[/red]] {content}')

    def title(self, content):
        self._console.print("=" * 45)
        self._console.print(content)
        self._console.print("=" * 45)

    def table(self, columns=[], data=[]):
        for column in columns:
            self._table.add_column(column)

        for row in data:
            values = [str(x) for x in row.values()]
            self._table.add_row(*values)

        self._console.print(self._table)

    def status(self, content):
        return self._console.status(content)
