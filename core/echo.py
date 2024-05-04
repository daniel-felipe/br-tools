from rich.console import Console


class Echo:
    def __init__(self):
        self._console = Console()

    def print(self, content):
        self._console.print(f'[[green]+[/green]] {content}')

    def error(self, content):
        self._console.print(f'[[red]-[/red]] {content}')

    def title(self, content):
        self._console.print("=" * 45)
        self._console.print(content)
        self._console.print("=" * 45)

    def status(self, content):
        return self._console.status(content)
