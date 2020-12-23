"""
Controller for getting all currencies supported by Nomics
https://nomics.com/docs/#operation/getCurrencies
"""
from typing import Type, List

from judah.destinations.database.model import DatabaseBaseModel
from judah.transformers.base import BaseTransformer

from .destination.model import Currencies
from .source import CurrenciesDataset
from ..abstract.controllers.bulk import NomicsBulkRestAPIToDatabaseController
from ..abstract.sources.bulk import NomicsBulkRestApiSource


class ControllerForCurrencies(NomicsBulkRestAPIToDatabaseController):
    """
    The controller for getting all supported currencies from Nomics
    """
    destination_model_class: Type[DatabaseBaseModel] = Currencies
    source_class: Type[NomicsBulkRestApiSource] = CurrenciesDataset
    interval_in_milliseconds: int = 24 * 60 * 60 * 1000  # 1 day
    transformer_classes: List[Type[BaseTransformer]] = []
