import json
import typing as t
import requests
from requests import Request
import re
import shlex
from urllib.parse import urlparse, parse_qs

from requests.sessions import PreparedRequest

class CURL:
    def __init__(self, command: t.Optional[str] = None, path: t.Optional[str] = None):
        assert command or path, "either cURL command text or path to cURL command is required"
        if path:
            with open(path, 'r') as file:
                command = file.read().strip()
        self.command = command
        self._parse()

    def _parse(self):
        parts = shlex.split(self.command)
        self._method = 'GET'
        self._headers = {}
        self._cookies = {}
        self._url = ''
        self._params = {}
        self._data = {}

        i = 1  # Skip 'curl'
        while i < len(parts):
            if parts[i] == '-H' or parts[i] == '--header':
                header = parts[i+1]
                key, value = header.split(':', 1)
                self._headers[key.strip()] = value.strip()
                i += 2
            elif parts[i] == '-X' or parts[i] == '--request':
                self._method = parts[i+1]
                i += 2
            elif parts[i] == '-d' or parts[i] in ['--data', '--data-raw']:
                try:
                    self._data = json.loads(parts[i+1])
                except json.JSONDecodeError:
                    self._data = parse_qs(parts[i+1])
                self._method = 'POST'  # Default to POST if data is present
                i += 2
            elif parts[i] == '--url':
                self._url = parts[i+1]
                i += 2
            elif parts[i].startswith('http'):
                self._url = parts[i]
                i += 1
            else:
                i += 1

        if self._url:
            parsed_url = urlparse(self._url)
            self._params = parse_qs(parsed_url.query)
            self._url = parsed_url._replace(query=None).geturl()

    @property
    def headers(self) -> t.Dict:
        return self._headers

    @property
    def cookies(self) -> t.Dict:
        return self._cookies

    @property
    def url(self) -> str:
        return self._url

    @property
    def method(self) -> str:
        return self._method

    @property
    def params(self) -> t.Dict:
        return self._params

    @property
    def data(self) -> t.Dict:
        return self._data

    def request(self) -> PreparedRequest:
        req = Request(
            method=self.method,
            url=self.url,
            headers=self.headers,
            params=self.params,
            data=self.data,
            cookies=self.cookies
        )
        return req.prepare()

    def execute(self):
        return requests.Session().send(self.request())

# Sample usage remains the same as provided in the original code
