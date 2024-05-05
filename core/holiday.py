from core.echo import Echo
from datetime import datetime
import requests
import sys


class Holiday:
    def __init__(self, year=None):
        if year is None:
            self._year = datetime.now().year
        self._url = f'https://brasilapi.com.br/api/feriados/v1/{self._year}'
        self._echo = Echo()
        self._content = {}

    def show(self):
        self._get()
        self._echo.title(f"Feriados de {self._year}")
        for holiday in self._content:
            formated_date = self._format_date(holiday['date'])
            if not self._is_future(holiday['date']):
                self._echo.error(f'{holiday["name"]} ({formated_date})')
                continue
            self._echo.print(f'{holiday["name"]} ({formated_date})')

    def _is_future(self, date):
        date = datetime.strptime(date, '%Y-%m-%d')
        return date > datetime.now()

    def _format_date(self, date):
        date = datetime.strptime(date, '%Y-%m-%d')
        return date.strftime('%d/%m/%Y')

    def _get(self):
        with self._echo.status('Buscando feriados...'):
            r = requests.get(self._url)

        if not r.ok:
            self._echo.error('Erro ao buscar feriados!')
            sys.exit(1)

        self._content = r.json()

        if 'erro' in self._content:
            self._echo.error('Feriado não encontrado!')
            sys.exit(1)
