"""Module containing a base controller class"""
import logging
import time
from datetime import datetime, timedelta
from typing import Type, Optional, Dict, Any, Iterator, List

from email_notifier import ExceptionNotifier
from selenium.common.exceptions import TimeoutException, WebDriverException
from urllib3.exceptions import ProtocolError

from app.core.destinations.base import DestinationBaseModel
from app.core.sources.base import BaseSource
from app.core.transformers.base import BaseTransformer

_KNOWN_EXTRACTION_EXCEPTIONS = (
    ProtocolError,
    WebDriverException,
    OSError,
    IndexError,
    TimeoutException,
    ConnectionError,
)

_KNOWN_TRANSFORMATION_EXCEPTIONS = (
    OSError,
)

_KNOWN_LOADING_EXCEPTIONS = (
    OSError,
)


class BaseController:
    """
    Class for the controller that gets data from a Source,
    transforms it
    and loads it in a destination basing on a given model
    """
    _source: BaseSource
    _interval: Optional[timedelta] = None
    _last_timestamp: Optional[datetime] = None

    destination_model_class: Type[DestinationBaseModel]
    source_class: Type[BaseSource]
    transformer_classes: List[Type[BaseTransformer]] = []
    interval_in_milliseconds: Optional[int] = None

    @classmethod
    def extract(cls) -> Iterator[Dict[Any, Any]]:
        """Initializes the extraction of the data from the source"""
        cls.__initialize()

        while True:
            try:
                start_time = datetime.now()
                yield from cls._query_source()

                if cls._interval is None:
                    break

                cls.__wait_for_interval_to_elapse(start_time=start_time)

            except _KNOWN_EXTRACTION_EXCEPTIONS as exp:
                logging.error(f'{cls._source.name} Extraction \n{exp}')
                yield from []
            except Exception as unknown_exception:
                notifier = ExceptionNotifier(subject=f'[Unknown] {cls._source.name} Extraction')
                notifier.notify(unknown_exception)

    @classmethod
    def transform(cls, data: Optional[Dict[Any, Any]]) -> Iterator[Optional[Dict[Any, Any]]]:
        """Transforms the data row by row into something else"""
        if data is None:
            yield None

        try:
            transformed_data = data

            for transformer in cls.transformer_classes:
                if isinstance(transformed_data, list):
                    list_output = []

                    for datum in transformed_data:
                        data_from_current_transformer = transformer.run(data=datum)

                        # spread the returned list into the final output
                        if isinstance(data_from_current_transformer, list):
                            list_output = list_output + data_from_current_transformer
                        # append the returned item to the list output
                        else:
                            list_output.append(data_from_current_transformer)

                    transformed_data = list_output
                else:
                    transformed_data = transformer.run(data=transformed_data)

            if isinstance(transformed_data, list):
                yield from transformed_data
            else:
                yield transformed_data
        except _KNOWN_TRANSFORMATION_EXCEPTIONS as exp:
            logging.error(f'{cls._source.name} Transformation \n{exp}')
            yield None
        except Exception as unknown_exception:
            notifier = ExceptionNotifier(subject=f'[Unknown] {cls._source.name} Transformation')
            notifier.notify(unknown_exception)

    @classmethod
    def load(cls, data: Optional[Dict[Any, Any]]) -> Iterator[Optional[Dict[Any, Any]]]:
        """Loads the data into the destination"""
        if data is None:
            yield None

        try:
            yield cls.destination_model_class.upsert(data=data)
        except _KNOWN_LOADING_EXCEPTIONS as exp:
            logging.error(f'{cls._source.name} Loading \n{exp}')
            yield None
        except Exception as unknown_exception:
            notifier = ExceptionNotifier(subject=f'[Unknown] {cls._source.name} Loading')
            notifier.notify(unknown_exception)

    @classmethod
    def _update_source(cls, *args, **kwargs) -> None:
        """
        Updates the configuration of the source especially
        those attributes that are bound to change
        """
        if not hasattr(cls, '_source'):
            cls._source = cls.source_class(
                attributes=cls.destination_model_class.get_attributes(),
                *args, **kwargs)

    @classmethod
    def _update_last_timestamp(cls):
        """Updates the last timestamp property of this class"""
        cls._last_timestamp = cls.destination_model_class.get_last_saved_timestamp()

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
        cls._update_last_timestamp()

    @classmethod
    def _query_source(cls, ) -> Iterator[Dict[Any, Any]]:
        """Queries the data source"""
        cls._update_source()
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
