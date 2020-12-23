"""
The Price, volume, market cap, and rank for all currencies across 1 hour, 1 day, 7 day, 30 day, 365 day,
and year to date intervals.
Current prices are updated every 10 seconds.
They are got from the /currencies/ticker endpoint
https://nomics.com/docs/#operation/getCurrenciesTicker
"""
import os
from typing import Dict, Any

from ..abstract.sources.paginated import NomicsPaginatedRestApiSource


class CurrenciesTickerDataset(NomicsPaginatedRestApiSource):
    """
    Class for getting all Price, volume, market cap, and rank for all currencies
    across 1 hour, 1 day, 7 day, 30 day, 365 day, and year to date intervals from Nomics API
    """
    name: str = 'v1/currencies/ticker'
    default_params: Dict[Any, Any] = {
        'key': os.getenv('NOMICS_API_KEY'),
        'convert': 'USD'
    }
