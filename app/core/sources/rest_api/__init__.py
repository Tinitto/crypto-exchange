"""Module containing configurations for the REST API data source"""
from typing import Iterator, Dict, Any

import requests

from ..base import BaseSource


class RestAPISource(BaseSource):
    """Base class for the REST API source"""

    def _get_data_url(self, *args, **kwargs):
        """Gets the url for given data from data source"""
        if self.base_uri is None or self.name is None:
            raise Exception("base_uri and name attributes should not be None")

        return f"{self.base_uri}"

    def _query_data_source(self, *args, **kwargs) -> Iterator[Dict[str, Any]]:
        """Queries a given start and end date and returns an iterator with data records"""
        url = self._get_data_url(*args, **kwargs)
        yield from requests.get(url=url).json().get('value')
