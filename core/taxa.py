from rich.console import Console
from rich.table import Table
import sys
import requests
from core.echo import Echo


class Taxa:
    _url = 'https://brasilapi.com.br/api/taxas/v1'

    def __init__(self):
        self._console = Console()
        self._echo = Echo()
        self._table = Table()
        self._content = None

    def show(self):
        self._get()
        self._echo.table(
            ['Taxa', 'Valor'],
            self._content
        )

    def _get(self):
        with self._console.status("[bold green]Buscando taxas[/bold green]"):
            r = requests.get(self._url)

        if not r.ok:
            sys.exit(1)

        self._content = r.json()
