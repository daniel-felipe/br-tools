import sys
import requests
from core.echo import Echo


class Cep:
    def __init__(self, cep):
        self.cep = cep
        self._echo = Echo()
        self._content = {}
        self._url = f'https://viacep.com.br/ws/{self.cep}/json/'

    def show(self):
        self._get()
        self._show_content()

    def _get(self):
        with self._echo.status("Buscando CEP..."):
            r = requests.get(self._url)

        if not r.ok:
            sys.exit(1)

        self._content = r.json()

    def _show_content(self):
        self._echo.title(f'CEP: {self._content.get("cep")}')

        for key, value in self._content.items():
            if not value or key == 'cep':
                continue

            self._echo.print(f'{key.capitalize()}: [green]{value}[/green]')
