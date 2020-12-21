"""Controller for getting quotes for all products by day session from the export site to and save to Database"""
from typing import Type, List

from judah.controllers.export_site_to_db.index_based import IndexBasedExportSiteToDBController
from judah.destinations.database.model import DatabaseBaseModel

from judah.sources.export_site.index_based import IndexBasedExportSiteSource
from judah.transformers.base import BaseTransformer
from judah.transformers.empty_string_transformer import EmptyStringTransformer

from .destination.model import QuoteByDaySession
from .source import QuotesByDaySessionDataset
from .transformers.datetime_transformers import QuotesUpdateDateTransformer, QuotesTradeDateTransformer, \
    QuotesUpdateTimeTransformer
from .transformers.field_value_alias_transformers import QuotesTradeTypeValueTransformer, \
    QuotesInstitutionsCodeValueTransformer, QuotesProductCodeValueTransformer


class ControllerForQuotesByDaySession(IndexBasedExportSiteToDBController):
    """
    The controller for the quotes for all products by day session resource
    got from the export site of the Tokyo Commodity Exchange
    """
    destination_model_class: Type[DatabaseBaseModel] = QuoteByDaySession
    source_class: Type[IndexBasedExportSiteSource] = QuotesByDaySessionDataset
    interval_in_milliseconds: int = 60 * 60 * 1000  # 1 hour
    transformer_classes: List[Type[BaseTransformer]] = [
        EmptyStringTransformer,
        QuotesUpdateDateTransformer,
        QuotesTradeDateTransformer,
        QuotesUpdateTimeTransformer,
        QuotesTradeTypeValueTransformer,
        QuotesInstitutionsCodeValueTransformer,
        QuotesProductCodeValueTransformer,
    ]
