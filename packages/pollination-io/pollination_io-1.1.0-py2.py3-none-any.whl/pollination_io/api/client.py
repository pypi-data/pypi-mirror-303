import os
import typing as t
from io import BytesIO

import requests

DEFAULT_HOST = os.getenv('POLLINATION_API_URL',
                         'https://api.pollination.solutions')


class ApiClient():

    def __init__(self, host: str = DEFAULT_HOST, api_token: str = None, jwt_token: str = None):
        if host[-1] == '/':
            host = host[:-1]

        self._host = host
        self.api_token = api_token
        self.jwt_token = jwt_token

    @property
    def api_token(self) -> str:
        return self._api_token

    @api_token.setter
    def api_token(self, value):
        self._api_token = self._validate_string_input(value)

    @property
    def jwt_token(self) -> str:
        return self._jwt_token

    @jwt_token.setter
    def jwt_token(self, value):
        self._jwt_token = self._validate_string_input(value)

    @staticmethod
    def _validate_string_input(value) -> str:
        if isinstance(value, str):
            if len(value) == 0:
                return None
            else:
                return value
        if value is None:
            return value
        raise ValueError(
            f'Expected instance of type str but got: {type(value)}')

    @property
    def is_authenticated(self) -> bool:
        return self.api_token is not None or self.jwt_token is not None

    @property
    def host(self) -> str:
        return self._host

    @property
    def headers(self):
        if self.api_token is not None:
            return {
                'x-pollination-token': self.api_token
            }
        elif self.jwt_token is not None:
            return {
                'Authorization': f'Bearer {self.jwt_token}'
            }
        return {}

    @property
    def session(self):
        s = requests.Session()
        s.headers = self.headers
        return s

    def _url_path(self, path: str) -> str:
        if not path.startswith('/'):
            path = '/' + path
        return self.host + path

    def get(self, path: str, params: t.Dict[str, t.Any] = {}) -> t.Dict[str, t.Any]:
        res = self.session.get(url=self._url_path(path), params=params)
        res.raise_for_status()
        try:
            return res.json()
        except:
            return res.text

    def post(self, path: str, json: t.Dict[str, t.Any]) -> t.Dict[str, t.Any]:
        res = self.session.post(url=self._url_path(path), json=json)
        res.raise_for_status()
        try:
            return res.json()
        except:
            return res.text

    def download_artifact(self, signed_url: str) -> BytesIO:
        res = requests.get(signed_url)
        res.raise_for_status()
        return BytesIO(res.content)
