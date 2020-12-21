"""Module containing a transformer class for transforming datetime values"""
from judah.transformers.datetime_transformer import DatetimeTransformer


class QuotesUpdateDateTransformer(DatetimeTransformer):
    """Transforms the update_date from %Y%m%d to %Y-%m-%d"""
    _datetime_field: str = 'update_date'
    _source_datetime_format: str = '%Y%m%d'


class QuotesTradeDateTransformer(DatetimeTransformer):
    """Transforms the trade_date from %Y%m%d to %Y-%m-%d"""
    _datetime_field: str = 'trade_date'
    _source_datetime_format: str = '%Y%m%d'


class QuotesUpdateTimeTransformer(DatetimeTransformer):
    """Transforms the update_time from %H%M%S to %H:%M:%S"""
    _datetime_field: str = 'update_time'
    _source_datetime_format: str = '%H%M%S'
    _destination_datetime_format: str = '%H:%M:%S'
