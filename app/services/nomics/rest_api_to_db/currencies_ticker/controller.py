"""
The Price, volume, market cap, and rank for all currencies across 1 hour, 1 day, 7 day, 30 day, 365 day,
and year to date intervals.
Current prices are updated every 10 seconds.
They are got from the /currencies/ticker endpoint
https://nomics.com/docs/#operation/getCurrenciesTicker
"""
from typing import Type, List

from judah.destinations.database.model import DatabaseBaseModel
from judah.transformers.base import BaseTransformer

from .destination.model import CurrenciesTicker
from .source import CurrenciesTickerDataset
from .transformers import CurrenciesTickerDictSplitter, CurrenciesTickerDataTypeConverter
from ..abstract.controllers.paginated import NomicsPaginatedRestAPIToDatabaseController
from ..abstract.sources.bulk import NomicsBulkRestApiSource


class ControllerForCurrenciesTicker(NomicsPaginatedRestAPIToDatabaseController):
    """
    The controller for getting all the Price, volume, market cap, and rank for all currencies
    across 1 hour, 1 day, 7 day, 30 day, 365 day, and year to date intervals
    """
    destination_model_class: Type[DatabaseBaseModel] = CurrenciesTicker
    source_class: Type[NomicsBulkRestApiSource] = CurrenciesTickerDataset
    interval_in_milliseconds: int = 10 * 1000  # 10 seconds
    transformer_classes: List[Type[BaseTransformer]] = [
        CurrenciesTickerDictSplitter,
        CurrenciesTickerDataTypeConverter,
    ]
