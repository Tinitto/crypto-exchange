"""
Module with the base source where the data is got in bulk
and cannot be paged through basing on any parameter
"""
import os
from typing import Iterator, Dict, Any, Optional

import requests
from judah.sources.base import BaseSource
from judah.sources.rest_api.date_based import RequestError


class NomicsBulkRestApiSource(BaseSource):
    """Source that picks data from the Nomics API without considering date, index or any such pagination"""
    base_uri: str = os.getenv('NOMICS_REST_API')
    response_data_key: Optional[str] = None
    default_headers: Optional[Dict[Any, Any]] = {}
    default_params: Dict[Any, Any] = {'key': os.getenv('NOMICS_API_KEY')}
    is_authenticated: bool = False

    def _authenticate(self):
        """A method to generate headers for authorization and update the default_headers"""
        self.is_authenticated = True

    def _get_headers(self) -> Dict[Any, Any]:
        """An overridable method to return headers use in the request"""
        return self.default_headers.copy()

    def _get_params(self, **kwargs) -> Dict[Any, Any]:
        """An overridable method to return query params dict to use in the request"""
        params = {**self.default_params, **kwargs}
        return params

    def _get_data_url(self):
        """Gets the url for given data from the REST API"""
        if self.base_uri is None or self.name is None:
            raise Exception("base_uri and name attributes should not be None")

        return f"{self.base_uri}/{self.name}"

    def _query_url(self, url: str, **kwargs) -> requests.Response:
        """Make a streamed requests GET request"""
        headers = self._get_headers()
        params = self._get_params(**kwargs)
        return requests.get(url=url, headers=headers, params=params, stream=True)

    def _extract_list_from_response(self, response: requests.Response):
        """Extracts the list data from the requests.Response object"""
        json_response = response.json()

        if self.response_data_key is not None:
            json_response = json_response.get(self.response_data_key)

        if isinstance(json_response, dict):
            yield json_response
        else:
            yield from json_response

    def _query_data_source(self, **kwargs) -> Iterator[Dict[str, Any]]:
        """Queries the endpoint in a streamed request and returns an iterator with data records"""
        url = self._get_data_url()

        if not self.is_authenticated:
            self._authenticate()

        response = self._query_url(url=url, **kwargs)
        if response.status_code in (401, 403, 400,):
            self.is_authenticated = False
            raise RequestError(message=response.text, status_code=response.status_code)
        elif response.ok:
            yield from self._extract_list_from_response(response=response)
        else:
            raise RequestError(message=response.text, status_code=response.status_code)
