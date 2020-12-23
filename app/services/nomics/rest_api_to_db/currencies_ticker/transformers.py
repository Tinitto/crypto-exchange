"""Transformers to be used for the currencies_ticker service"""
from datetime import datetime, date
from typing import List, Dict, Type, Any

from app.services.abstract.transformers.data_type_converter import DataTypeConverter
from app.services.abstract.transformers.dict_splitter import DictSplitter


class CurrenciesTickerDictSplitter(DictSplitter):
    """
    Splits the currencies ticker datum into 5:
    one for each interval of 1d, 7d, 30d, 365d, ytd
    """
    _new_key: str = 'interval'
    _keys_for_split: List[str] = ['1d', '7d', '30d', '365d', 'ytd']


class CurrenciesTickerDataTypeConverter(DataTypeConverter):
    """
    Converts the values for the given fields to the given data types
    """
    _value_type_map: Dict[str, Type[Any]] = {
        "price": float,
        "price_date": date,
        "price_timestamp": datetime,
        "circulating_supply": float,
        "max_supply": float,
        "market_cap": float,
        "num_exchanges": float,
        "num_pairs": float,
        "num_pairs_unmapped": float,
        "first_candle": datetime,
        "first_order_book": datetime,
        "first_trade": datetime,
        "first_priced_at": datetime,
        "rank": int,
        "rank_delta": int,
        "high": float,
        "high_timestamp": datetime,
        "volume": float,
        "price_change": float,
        "price_change_pct": float,
        "volume_change": float,
        "volume_change_pct": float,
        "market_cap_change": float,
        "market_cap_change_pct": float
    }