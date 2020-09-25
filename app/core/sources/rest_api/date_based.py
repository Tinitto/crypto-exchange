"""Module containing base class for date-based REST API sources"""

from datetime import date
from typing import Iterator, Dict, Any, Optional

import requests

from app.core.sources.base.date_based import DateBasedBaseSource


class DateBasedRestAPISource(DateBasedBaseSource):
    """Base class for date-based REST API sources"""
    response_data_key: Optional[str] = None

    def _get_data_url(self, start_date: date, end_date: date):
        """Gets the url for given data from data source"""
        if self.base_uri is None or self.name is None:
            raise Exception("base_uri and name attributes should not be None")

        return f"{self.base_uri}"

    def _query_data_source(self, start_date: date, end_date: date) -> Iterator[Dict[str, Any]]:
        """Queries a given start and end date and returns an iterator with data records"""
        url = self._get_data_url(start_date=start_date, end_date=end_date)

        if self.response_data_key is None:
            yield from requests.get(url=url).json()
        else:
            yield from requests.get(url=url).json().get(self.response_data_key)
