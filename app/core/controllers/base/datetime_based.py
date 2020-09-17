"""Module containing Base class for datetime-based controllers"""

from datetime import datetime
from typing import Optional, Type, Iterator, Dict, Any

from app.core.controllers.base import BaseController
from app.core.sources.base.datetime_based import DatetimeBasedBaseSource


class DatetimeBasedBaseController(BaseController):
    """Base controller class for datetime-based data sources"""
    _source: DatetimeBasedBaseSource

    start_datetime: Optional[datetime] = None
    end_datetime: Optional[datetime] = None
    source_class: Type[DatetimeBasedBaseSource]

    @classmethod
    def _query_source(cls, ) -> Iterator[Dict[Any, Any]]:
        """Queries the data source"""
        cls._update_source(start_datetime=cls.start_datetime, end_datetime=cls.end_datetime)
        return cls._source.get()
