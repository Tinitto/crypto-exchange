"""Module containing the base transformer for data"""
from typing import Dict, Any


class BaseTransformer:
    """
    The base class for all data transformers that receive a dictionary
    and return a transformed dictionary
    """

    @classmethod
    def run(cls, data: Dict[Any, Any]) -> Dict[Any, Any]:
        """This transforms the data"""
        return data
