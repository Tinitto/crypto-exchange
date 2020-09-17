"""Module containing base class for datetime-based REST API sources"""

from datetime import datetime
from typing import Iterator, Dict, Any

import requests

from app.core.sources.base.datetime_based import DatetimeBasedBaseSource


class DatetimeBasedRestAPISource(DatetimeBasedBaseSource):
    """Base class for datetime-based REST API sources"""

    def _get_data_url(self, start_datetime: datetime, end_datetime: datetime):
        """Gets the url for given data from data source"""
        if self.base_uri is None or self.name is None:
            raise Exception("base_uri and name attributes should not be None")

        return f"{self.base_uri}"

    def _query_data_source(self, start_datetime: datetime, end_datetime: datetime) -> Iterator[Dict[str, Any]]:
        """Queries a given start and end date and returns an iterator with data records"""
        url = self._get_data_url(start_datetime=start_datetime, end_datetime=end_datetime)
        yield from requests.get(url=url).json().get('value')
