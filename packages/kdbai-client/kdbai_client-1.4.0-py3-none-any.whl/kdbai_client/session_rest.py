from typing import Any, Dict, List
from urllib import parse

import requests

from .constants import Headers, RestPath
from .database_rest import DatabaseRest
from .kdbai_exception import KDBAIException
from .utils import process_response
from .version import check_version


MAX_QIPC_SERIALIZATION_SIZE = 10*1024*1024  # 10MB

class SessionRest:
    """Session represents a REST connection to a KDB.AI instance."""

    def __init__(
        self,
        api_key = None,
        *,
        endpoint: str
    ):
        """Create a REST API connection to a KDB.AI endpoint.

        Args:
            api_key (str): API Key to be used for authentication.
            endpoint (str): Server endpoint to connect to.

        Example:
            Open a session on KDB.AI Cloud with an api key:

            ```python
            session = Session(endpoint='YOUR_INSTANCE_ENDPOINT', api_key='YOUR_API_KEY')
            ```

            Open a session on a custom KDB.AI instance on http://localhost:8082:

            ```python
            session = Session(endpoint='http://localhost:8082', mode='rest')
            ```
        """
        self.api_key = api_key
        self.endpoint = endpoint
        self.headers = dict()
        if self.api_key:
            self.headers['X-Api-Key'] = self.api_key
        self._is_alive: bool = True
        self._check_endpoint()
        self._check_readiness()
        check_version(self.version())

    def _check_endpoint(self):
        try:
            url = parse.urlparse(self.endpoint)
            assert url.scheme in ('http', 'https')
            assert url.netloc != ''
        except Exception:
            raise KDBAIException(f'Invalid URL: {self.endpoint}.')
        return True

    def _check_readiness(self):
        try:
            response = self._send_request(requests.get, self._build_url(RestPath.READY), headers=self.headers)
            assert response.status_code == 200
        except Exception:
            tmp = None if self.api_key is None else self.api_key[:10]
            raise KDBAIException(
                f'Failed to open a session on {self.endpoint} using API key with prefix {tmp}. '
                'Please double check your `endpoint` and `api_key`.'
                )

    def _build_url(self, path):
        return f'{self.endpoint}{path}'

    def _build_headers(self, headers):
        return {**headers, **self.headers}

    def close(self) -> None:
        """Close connection to the server"""
        self._is_alive = False

    def version(self) -> Dict[str, Any]:
        """Retrieve version information from server"""
        return self._send_request(requests.get, self._build_url(RestPath.VERSION), headers=self.headers).json()

    def create_database(self, database: str) -> DatabaseRest:
        """Create a new database"""
        response = self._send_request(requests.post,
                                      self._build_url(RestPath.DATABASE_CREATE),
                                      json={'database': database},
                                      headers=self._build_headers(Headers.JSON_JSON))
        process_response(response, expected_status_code=201)
        return DatabaseRest(name=database, session=self, tables_meta=dict())

    def databases(self, include_tables: bool) -> List[DatabaseRest]:
        """List databases"""
        response = self._send_request(requests.get,
                                      self._build_url(RestPath.DATABASE_LIST),
                                      headers=self._build_headers(Headers.ACCEPT_JSON))
        result = process_response(response, expected_status_code=200)['result']
        if include_tables:
            return [self.database(db_name) for db_name in result]

        return [DatabaseRest(name=db_name, session=self, tables_meta=dict()) for db_name in result]

    def database(self, database: str) -> DatabaseRest:
        """Fetch a database"""
        response = self._send_request(requests.get,
                                      self._build_url(RestPath.DATABASE_GET.format(db_name=database)),
                                      headers=self._build_headers(Headers.ACCEPT_JSON))
        result = process_response(response, expected_status_code=200)['result']
        return DatabaseRest(name=database, session=self, tables_meta=result.get('tables') or dict())

    def _send_request(self, func, *args, **kwargs):
        """Send REST request"""
        if not self._is_alive:
            raise RuntimeError('Attempted to use closed session')
        try:
            return func(*args, **kwargs)
        except requests.exceptions.ConnectionError:
            raise RuntimeError('Error during request, make sure KDB.AI server running')
