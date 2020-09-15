"""Utility Functions centered around data"""
from typing import Any


def convert_empty_string_to_none(value: Any):
    """Converts a given empty string to None"""
    if value == '':
        return None

    return value