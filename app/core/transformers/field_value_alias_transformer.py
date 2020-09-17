"""Module containing a data transformer that exchanges field values for their aliases"""
from typing import Dict, Any

from app.core.transformers.base import BaseTransformer
from app.core.utils.data import replace_keys_with_aliases


class FieldValueAliasTransformer(BaseTransformer):
    """Changes the value of a given field in the data passed to it to its alias"""
    _alias_map: Dict[str, str] = {}
    _field_name: str

    @classmethod
    def run(cls, data: Dict[Any, Any]) -> Dict[Any, Any]:
        """Replaces the value of a given field in the data with its alias"""
        data_copy = data.copy()
        field_value = data_copy.get(cls._field_name, None)

        data_copy[cls._field_name] = cls._alias_map.get(field_value, field_value)

        return data_copy
