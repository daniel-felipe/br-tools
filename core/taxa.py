from rich.console import Console
from rich.table import Table
import sys
import requests


class Taxa:
    _url = 'https://brasilapi.com.br/api/taxas/v1'

    def __init__(self):
        self._console = Console()
        self._table   = Table()
        self._content = None

    def show(self):
        self._get()
        self._build_table(self._content)
        self._show_table()

    def _get(self):
        try:
            with self._console.status("[bold green]Buscando taxas...[/bold green]"):
                r = requests.get(self._url)
        except:
            sys.exit(1) 
        self._content = r.json()
    
    def _build_table(self, data):
        self._table.add_column('Taxa') 
        self._table.add_column('Valor')
        for taxa in data:
            name, value = taxa.get('nome'), taxa.get('valor')
            self._table.add_row(name, str(value))

    def _show_table(self):
        self._console.print(self._table)

