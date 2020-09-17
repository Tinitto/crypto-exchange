"""Module containing Base class for date-based controllers"""

from datetime import date
from typing import Optional, Type, Iterator, Dict, Any

from app.core.controllers.base import BaseController
from app.core.sources.base.date_based import DateBasedBaseSource


class DateBasedBaseController(BaseController):
    """Base controller class for date-based data sources"""
    _source: DateBasedBaseSource

    start_date: Optional[date] = None
    end_date: Optional[date] = None
    source_class: Type[DateBasedBaseSource]

    @classmethod
    def _query_source(cls, ) -> Iterator[Dict[Any, Any]]:
        """Queries the data source"""
        cls._update_source(start_date=cls.start_date, end_date=cls.end_date)
        return cls._source.get()