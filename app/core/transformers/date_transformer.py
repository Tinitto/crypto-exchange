"""Module contains the class that transforms data by formatting the date"""
from typing import Dict, Any

from app.core.transformers.base import BaseTransformer
from app.core.utils.dates import change_date_format


class DateTransformer(BaseTransformer):
    """Transforms the format of the date field in a given data dictionary"""
    _date_field: str = 'Date'
    _source_date_format: str = '%m/%d/%Y'
    _destination_date_format: str = '%Y-%m-%d'

    @classmethod
    def run(cls, data: Dict[Any, Any]):
        """Transforms the dates to the right format"""
        data_copy = data.copy()
        date_value = data_copy.get(cls._date_field, None)

        if date_value is not None:
            data_copy[cls._date_field] = change_date_format(
                date_value=date_value, old=cls._source_date_format, new=cls._destination_date_format)

        return data_copy
