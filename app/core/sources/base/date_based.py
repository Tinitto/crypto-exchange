"""Module containing base class for date based sources"""

from datetime import date
from typing import Optional, Iterator, Dict, Any

from app.core.sources.base import BaseSource
from app.core.utils.datetime import update_date


class DateBasedBaseSource(BaseSource):
    default_batch_size_in_days: int = 7
    start_date: Optional[date] = None
    end_date: Optional[date] = None

    def get(self) -> Iterator[Dict[str, Any]]:
        """Returns data from a given date to a given date as an iterator"""
        start_date = self._get_next_start_date()
        end_date = self._get_next_end_date()

        if end_date < start_date:
            yield from []
        else:
            yield from self._query_data_source(start_date=start_date, end_date=end_date)

            self.start_date = self._get_next_start_date(days_to_increment_by=self.default_batch_size_in_days)

    def _query_data_source(self, start_date: date, end_date: date) -> Iterator[Dict[str, Any]]:
        """Queries a given start and end date and returns an iterator with data records"""
        raise NotImplementedError(
            'Implement the _query_data_source method to return an iterator of dictionaries')

    def _get_next_end_date(self, days_to_increment_by: int = 0, days_to_decrement_by: int = 0) -> date:
        """Gets the next end date in the given iteration"""
        initial_date: Optional[date] = self.end_date

        if not isinstance(initial_date, date):
            if isinstance(self.start_date, date):
                initial_date = self.start_date
                days_to_increment_by = self.default_batch_size_in_days + days_to_increment_by
            else:
                initial_date = date.today()

        return update_date(date_to_update=initial_date, days_to_decrement_by=days_to_decrement_by,
                           days_to_increment_by=days_to_increment_by)

    def _get_next_start_date(self, days_to_increment_by: int = 0, days_to_decrement_by: int = 0) -> date:
        """Gets the next start date in the given iteration"""
        initial_date: Optional[date] = self.start_date

        if not isinstance(initial_date, date):
            initial_date = self.end_date if isinstance(self.end_date, date) else date.today()
            days_to_decrement_by = self.default_batch_size_in_days + days_to_decrement_by

        return update_date(date_to_update=initial_date, days_to_decrement_by=days_to_decrement_by,
                           days_to_increment_by=days_to_increment_by)
