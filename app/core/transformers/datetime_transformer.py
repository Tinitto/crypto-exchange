"""Module contains the class that transforms data by formatting the datetime"""
from typing import Dict, Any

from app.core.transformers.base import BaseTransformer
from app.core.utils.datetime import change_datetime_format


class DatetimeTransformer(BaseTransformer):
    """Transforms the format of the datetime field in a given data dictionary"""
    _datetime_field: str = 'Date'
    _source_datetime_format: str = '%m/%d/%Y'
    _destination_datetime_format: str = '%Y-%m-%d'

    @classmethod
    def run(cls, data: Dict[Any, Any]):
        """Transforms the date_times to the right format"""
        data_copy = data.copy()
        date_value = data_copy.get(cls._datetime_field, None)

        if date_value is not None:
            data_copy[cls._datetime_field] = change_datetime_format(
                date_value=date_value, old=cls._source_datetime_format, new=cls._destination_datetime_format)

        return data_copy
