import os
from datetime import date, timedelta, datetime
from typing import Optional


def convert_date_to_string(
        date_value: date, date_format: str = '%Y-%m-%dT%T%ZZ') -> str:
    """Converts a date to the expected string"""
    return date_value.strftime(date_format)


def get_default_historical_start_date() -> Optional[date]:
    """Extracts the default start_date from the environment"""
    start_year = os.getenv('HISTORICAL_STARTING_YEAR', None)
    start_month = int(os.getenv('HISTORICAL_STARTING_MONTH', 1))
    start_day = int(os.getenv('HISTORICAL_STARTING_DAY', 1))

    if start_year is None:
        return None

    return date(year=int(start_year), month=start_month, day=start_day)


def update_date(date_to_update: date, days_to_increment_by: int, days_to_decrement_by: int):
    """Updates a given date by incrementing and/or decrementing it"""
    return date_to_update + timedelta(days=days_to_increment_by) - timedelta(days=days_to_decrement_by)


def update_datetime(datetime_to_update: datetime, ms_to_increment_by: int, ms_to_decrement_by: int):
    """Updates a given datetime by incrementing and/or decrementing it by given milliseconds"""
    return (
            datetime_to_update
            + timedelta(milliseconds=ms_to_increment_by)
            - timedelta(milliseconds=ms_to_decrement_by)
    )


def change_datetime_format(date_value: str, old: str, new: str):
    """Converts a date string's format to another format"""
    return datetime.strptime(date_value, old).strftime(new)
