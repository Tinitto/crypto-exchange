"""Module that contains a transformer that converts values to given data types"""
import re
from datetime import timedelta, datetime, date
from typing import Dict, Type, Any

from judah.transformers.base import BaseTransformer

from .utils import convert_string_to_timedelta


_DECIMAL_SECONDS_REGEX = re.compile(r'(\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d)(.*)(Z)')


class DataTypeConverter(BaseTransformer):
    """Transforms values to given types as given by the value_type_map dict"""
    _value_type_map: Dict[str, Type[Any]] = {}
    _datetime_format: str = '%Y-%m-%dT%H:%M:%SZ'
    _date_format: str = '%Y-%m-%dT%H:%M:%SZ'

    @classmethod
    def _clean_datetime_value(cls, value: str):
        """Cleans the datetime value to an appropriate datetime string"""
        return _DECIMAL_SECONDS_REGEX.sub(r'\1\3', value)

    @classmethod
    def _get_converted_value(cls, key: Any, value: Any):
        """Gets the type converted value"""
        cast_type = cls._value_type_map.get(key, None)

        if cast_type is None or value is None:
            return value
        elif cast_type == timedelta:
            return convert_string_to_timedelta(value)
        elif cast_type == datetime and isinstance(value, str):
            return datetime.strptime(cls._clean_datetime_value(value), cls._datetime_format)
        elif cast_type == date and isinstance(value, str):
            return datetime.strptime(cls._clean_datetime_value(value), cls._date_format)

        return cast_type(value)

    @classmethod
    def run(cls, data: Dict[Any, Any]) -> Dict[Any, Any]:
        """Method to convert any value to the given data type"""
        return {key: cls._get_converted_value(key, value) for key, value in data.items()}
