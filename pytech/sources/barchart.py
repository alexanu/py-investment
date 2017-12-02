import os
from typing import Iterable

from sources.restclient import RestClient
import pytech.utils as utils


class BarChartClient(RestClient):
    def __init__(self, api_key: str = None, **kwargs):
        super().__init__()
        self._base_url = 'http://marketdata.websol.barchart.com'
        self.api_key = os.environ.get('BARCHART_API_KEY', api_key)

        if self.api_key is None:
            raise KeyError('Must set BARCHART_API_KEY.')

        self._headers = {
            'X-OnDemand-Client': 'pytech-bc'
        }

    @property
    def base_url(self):
        return self._base_url

    @property
    def headers(self):
        return self._headers

    def quote(self, symbols: Iterable[str], fields: Iterable[str] = None):
        url = 'getQuote.json'
        if not utils.is_iterable(symbols):
            symbols = (symbols,)

        params = {
            'apikey': self.api_key,
            'symbols': ','.join(symbols)
        }

        if fields is not None:
            if not utils.is_iterable(fields):
                fields = (fields,)
            params['fields'] = ','.join(fields)

        resp = self._request(url, params=params)

        return resp.json()

