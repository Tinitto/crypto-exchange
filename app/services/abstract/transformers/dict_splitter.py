"""Module that contains a transformer that splits a dict into a number of other dicts basing on given keys"""
from typing import List, Dict, Any

from judah.transformers.base import BaseTransformer


class DictSplitter(BaseTransformer):
    """Splits a given dictionary into a given number of dictionaries with common fields"""
    _new_key: str
    _keys_for_split: List[str] = []

    @classmethod
    def run(cls, data: Dict[Any, Any]) -> List[Dict[Any, Any]]:
        """Method to split a single dict into multiple dicts"""
        common_dict = {key: value for key, value in data.items() if key not in cls._keys_for_split}
        return [{**common_dict, cls._new_key: key, **data.get(key, {})} for key in cls._keys_for_split]
