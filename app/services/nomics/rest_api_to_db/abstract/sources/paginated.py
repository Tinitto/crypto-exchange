"""Base class for paginated REST API sources for Nomics API"""

from typing import Iterator, Dict, Any

import requests
from judah.sources.rest_api.date_based import RequestError

from app.services.nomics.rest_api_to_db.abstract.sources.base import NomicsRestApiSource


class EmptyResponse(Exception):
    pass


class NomicsPaginatedRestApiSource(NomicsRestApiSource):
    """
    Class for getting all Price, volume, market cap, and rank for all currencies across 1 hour, 1 day, 7 day, 30 day,
    365 day, and year to date intervals from Nomics API
    """
    page_size: int = 100
    page: int = 1

    def _get_params(self, **kwargs) -> Dict[Any, Any]:
        """Gets the params to add to the url"""
        params = super()._get_params(**kwargs)
        return {'page': self.page, 'per-page': self.page_size, **params}

    def _query_data_source(self, **kwargs) -> Iterator[Dict[str, Any]]:
        """
        Queries the endpoint in a streamed request and returns an iterator with data records
        """
        url = self._get_data_url()

        if not self.is_authenticated:
            self._authenticate()

        while 'response_is_not_empty':
            response = self._query_url(url=url, **kwargs)

            if response.status_code in (401, 403, 400,):
                self.is_authenticated = False

            if not response.ok:
                raise RequestError(message=response.text, status_code=response.status_code)

            try:
                yield from self._extract_list_from_response(response=response)
                self.page += 1
            except EmptyResponse:
                yield from []
                self.page = 1
                break

    def _extract_list_from_response(self, response: requests.Response):
        """Extracts the list data from the requests.Response object"""
        json_response = response.json()

        if len(json_response) == 0:
            raise EmptyResponse("Response returned was empty")

        if self.response_data_key is not None:
            json_response = json_response.get(self.response_data_key)

        if isinstance(json_response, dict):
            yield json_response
        else:
            yield from json_response
