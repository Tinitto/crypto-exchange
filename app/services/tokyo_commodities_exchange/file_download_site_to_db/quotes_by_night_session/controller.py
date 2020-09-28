"""Controller for getting quotes for all products by night session from the export site to and save to Database"""
from typing import Type, List

from app.core.controllers.file_download_site_to_db.index_based import IndexBasedFileDownloadSiteToDBController
from app.core.destinations.database.model import DatabaseBaseModel

from app.core.sources.file_download_site.datetime_based import DatetimeBasedFileDownloadSiteSource
from app.core.transformers.base import BaseTransformer
from app.core.transformers.empty_string_transformer import EmptyStringTransformer

from .destination.model import QuoteByNightSession
from .source import QuotesByNightSessionDataset
from .transformers.datetime_transformers import QuotesUpdateDateTransformer, QuotesTradeDateTransformer, \
    QuotesUpdateTimeTransformer
from .transformers.field_value_alias_transformers import QuotesTradeTypeValueTransformer, \
    QuotesInstitutionsCodeValueTransformer, QuotesProductCodeValueTransformer


class ControllerForQuotesByNightSession(IndexBasedFileDownloadSiteToDBController):
    """
    The controller for the quotes for all products by night session resource
    got from the export site of the Tokyo Commodity Exchange
    """
    destination_model_class: Type[DatabaseBaseModel] = QuoteByNightSession
    source_class: Type[DatetimeBasedFileDownloadSiteSource] = QuotesByNightSessionDataset
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
