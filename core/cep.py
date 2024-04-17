import sys
import requests
from rich.console import Console

class Cep:
    def __init__(self, cep):
        self.cep = cep
        self._console = Console()
        self._content = {}
        self._url = f'https://viacep.com.br/ws/{self.cep}/json/'

    def show(self):
        self._get()
        self._show_content()

    def _get(self):
        try:
            with self._console.status("[bold green]Buscando CEP...[/bold green]"):
                r = requests.get(self._url)
        except:
            sys.exit(1)
        self._content = r.json()
    
    def _show_content(self):
        self._console.print('=' * 30, style='bold yellow')
        self._console.print(f'[bold yellow]CEP:[/bold yellow] {self._content.get("cep")}')
        self._console.print('=' * 30, style='bold yellow')
        for key, value in self._content.items():
            if not value:
                continue
            self._console.print(f'[yellow][+][/yellow] {key.capitalize()}: [green]{value}[/green]')

