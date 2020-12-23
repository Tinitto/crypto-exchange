"""Base source for Nomics API resource"""

import os
from typing import Iterator, Dict, Any, Optional

import requests
from judah.sources.base import BaseSource
from judah.sources.rest_api.date_based import RequestError


class NomicsRestApiSource(BaseSource):
    """Base Source class for where the source picks data from the Nomics API"""
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

    def _extract_list_from_response(self, response: requests.Response) -> Iterator[Dict[str, Any]]:
        """Extracts the list data from the requests.Response object"""
        raise NotImplementedError('The _extract_list_from_response method ought to be implemented')

    def _query_data_source(self, *args, **kwargs) -> Iterator[Dict[str, Any]]:
        raise NotImplementedError('The _query_data_source method ought to be implemented')
