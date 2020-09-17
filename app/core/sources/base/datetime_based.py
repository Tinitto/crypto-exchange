"""Module containing base class for datetime based sources"""

from datetime import datetime
from typing import Optional, Iterator, Dict, Any

from app.core.sources.base import BaseSource
from app.core.utils.datetime import update_datetime


class DatetimeBasedBaseSource(BaseSource):
    default_batch_size_in_milliseconds: int = 60000  # 1 minute
    start_datetime: Optional[datetime] = None
    end_datetime: Optional[datetime] = None

    def get(self) -> Iterator[Dict[str, Any]]:
        """Returns data from a given datetime to a given date as an iterator"""
        start_datetime = self._get_next_start_datetime()
        end_datetime = self._get_next_end_datetime()

        if end_datetime < start_datetime:
            yield from []
        else:
            yield from self._query_data_source(start_datetime=start_datetime, end_datetime=end_datetime)

            self.start_datetime = self._get_next_start_datetime(
                ms_to_increment_by=self.default_batch_size_in_milliseconds)

    def _query_data_source(self, start_datetime: datetime, end_datetime: datetime) -> Iterator[Dict[str, Any]]:
        """Queries a given start and end datetime and returns an iterator with data records"""
        raise NotImplementedError(
            'Implement the _query_data_source method to return an iterator of dictionaries')

    def _get_next_end_datetime(self, ms_to_increment_by: int = 0, ms_to_decrement_by: int = 0) -> datetime:
        """Gets the next end datetime in the given iteration"""
        initial_datetime: Optional[datetime] = self.end_datetime

        if not isinstance(initial_datetime, datetime):
            if isinstance(self.start_datetime, datetime):
                initial_datetime = self.start_datetime
                days_to_increment_by = self.default_batch_size_in_milliseconds + ms_to_increment_by
            else:
                initial_datetime = datetime.now()

        return update_datetime(datetime_to_update=initial_datetime, ms_to_decrement_by=ms_to_decrement_by,
                               ms_to_increment_by=ms_to_increment_by)

    def _get_next_start_datetime(self, ms_to_increment_by: int = 0, ms_to_decrement_by: int = 0) -> datetime:
        """Gets the next start date in the given iteration"""
        initial_datetime: Optional[datetime] = self.start_datetime

        if not isinstance(initial_datetime, datetime):
            initial_datetime = self.end_datetime if isinstance(self.end_datetime, datetime) else datetime.now()
            ms_to_decrement_by = self.default_batch_size_in_milliseconds + ms_to_decrement_by

        return update_datetime(datetime_to_update=initial_datetime, ms_to_decrement_by=ms_to_decrement_by,
                               ms_to_increment_by=ms_to_increment_by)
