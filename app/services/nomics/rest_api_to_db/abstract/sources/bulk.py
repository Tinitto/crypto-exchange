"""
Module with the base source where the data is got in bulk
and cannot be paged through basing on any parameter
"""
from typing import Iterator, Dict, Any

import requests
from judah.sources.rest_api.date_based import RequestError

from app.services.nomics.rest_api_to_db.abstract.sources.base import NomicsRestApiSource


class NomicsBulkRestApiSource(NomicsRestApiSource):
    """Source that picks data from the Nomics API without considering date, index or any such pagination"""

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

        if not response.ok:
            raise RequestError(message=response.text, status_code=response.status_code)

        yield from self._extract_list_from_response(response=response)
