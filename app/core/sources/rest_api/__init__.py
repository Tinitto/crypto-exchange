"""Module containing configurations for the REST API data source"""

from datetime import date
from typing import Iterator, Dict, Any

import requests

from ..base import BaseSource


class RestAPISource(BaseSource):
    """Base class for the REST API source"""

    def _get_data_url(self, start_date: date, end_date: date):
        """Gets the url for given data from TenneT"""
        if self.base_uri is None or self.name is None:
            raise Exception("base_uri and name attributes should not be None")

        return f"{self.base_uri}"

    def _query_data_source(self, start_date: date, end_date: date) -> Iterator[Dict[str, Any]]:
        """Queries a given start and end date and returns an iterator with data records"""
        url = self._get_data_url(start_date=start_date, end_date=end_date)
        yield from requests.get(url=url).json().get('value')
