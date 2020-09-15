"""Module containing a base controller class"""

import time
from datetime import date, datetime, timedelta
from typing import Type, Optional, Dict, Any, Iterator

from app.core.destinations.base import DestinationBaseModel
from app.core.sources.base import BaseSource


class BaseController:
    """
    Class for the controller that gets data from a Source,
    transforms it
    and loads it in a destination basing on a given model
    """
    _source: BaseSource
    _interval: Optional[timedelta] = None

    destination_model_class: Type[DestinationBaseModel]
    source_class: Type[BaseSource]
    interval_in_milliseconds: Optional[int] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None

    @classmethod
    def extract(cls) -> Iterator[Dict[Any, Any]]:
        """Initializes the extraction of the data from the source"""
        cls.__initialize()

        while True:
            start_time = datetime.now()
            yield from cls.__query_source()

            if cls._interval is None:
                break

            cls.__wait_for_interval_to_elapse(start_time=start_time)

    @classmethod
    def load(cls, data: Dict[Any, Any]) -> Iterator[Dict[Any, Any]]:
        """Loads the data into the destination"""
        yield cls.destination_model_class.upsert(data=data)

    @classmethod
    def transform(cls, data: Dict[Any, Any]) -> Iterator[Dict[Any, Any]]:
        """Transforms the data row by row into something else"""
        yield data

    @classmethod
    def __update_source(cls, start_date: Optional[date] = None, end_date: Optional[date] = None) -> None:
        """
        Updates the configuration of the source especially
        those attributes that are bound to change
        """
        if not hasattr(cls, '_source'):
            cls._source = cls.source_class(
                attributes=cls.destination_model_class.get_attributes(),
                start_date=start_date,
                end_date=end_date)

    @classmethod
    def __update_interval(cls) -> None:
        """Updates the _interval basing on the interval_in_milliseconds"""
        if isinstance(cls.interval_in_milliseconds, int):
            cls._interval = timedelta(milliseconds=cls.interval_in_milliseconds)

    @classmethod
    def __initialize(cls) -> None:
        """Creates the tables if these are non-existent and updates the _interval if necessary"""
        cls.__update_interval()
        cls.destination_model_class.initialize()

    @classmethod
    def __query_source(cls, ) -> Iterator[Dict[Any, Any]]:
        """Queries the data source"""
        cls.__update_source(start_date=cls.start_date, end_date=cls.end_date)
        return cls._source.get()

    @classmethod
    def __wait_for_interval_to_elapse(cls, start_time: datetime) -> None:
        """Waits for the interval to elapse before starting again"""
        if not isinstance(cls._interval, timedelta):
            return

        time_used_up_so_far = datetime.now() - start_time
        seconds_left_off_interval = (cls._interval - time_used_up_so_far).total_seconds()

        if seconds_left_off_interval > 0:
            time.sleep(seconds_left_off_interval)
