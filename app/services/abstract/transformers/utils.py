"""Simple utils for transformers"""
import re
from datetime import timedelta

_HH_MM_REGEX = re.compile(r'(\d+):(\d+)')


def convert_string_to_timedelta(value: str):
    """Converts time duration like HH:MM to a timedelta"""
    hours, minutes = _HH_MM_REGEX.match(value).groups()
    return timedelta(hours=float(hours), minutes=float(minutes))
