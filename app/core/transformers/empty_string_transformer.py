"""Module contains transformer class for transforming empty strings to something else"""
from typing import Dict, Any

from app.core.transformers.base import BaseTransformer
from app.core.utils.data import remove_empty_string_values


class EmptyStringTransformer(BaseTransformer):
    """Transformer class for transforming empty strings to some thing else"""
    replacement: Any = None

    @classmethod
    def run(cls, data: Dict[Any, Any]) -> Dict[Any, Any]:
        """Converts empty strings into some other value"""
        return {
            key: remove_empty_string_values(value=value, replacement=cls.replacement)
            for key, value in data.items()
        }
