"""Module containing base class for datetime-based REST API sources"""

from datetime import datetime
from typing import Iterator, Dict, Any, Optional

import requests
from email_notifier import ExceptionNotifier

from app.core.sources.base.datetime_based import DatetimeBasedBaseSource


class DatetimeBasedRestAPISource(DatetimeBasedBaseSource):
    """Base class for datetime-based REST API sources"""
    response_data_key: Optional[str] = None

    def _get_data_url(self, start_datetime: datetime, end_datetime: datetime):
        """Gets the url for given data from data source"""
        if self.base_uri is None or self.name is None:
            raise Exception("base_uri and name attributes should not be None")

        return f"{self.base_uri}"

    def _query_data_source(self, start_datetime: datetime, end_datetime: datetime) -> Iterator[Dict[str, Any]]:
        """Queries a given start and end date and returns an iterator with data records"""
        url = self._get_data_url(start_datetime=start_datetime, end_datetime=end_datetime)

        try:
            if self.response_data_key is None:
                yield from requests.get(url=url).json()
            else:
                yield from requests.get(url=url).json().get(self.response_data_key)
        except TypeError as exp:
            exception_notifier = ExceptionNotifier(subject="Empty Response")
            exception_notifier.notify(exp)
            yield from []
