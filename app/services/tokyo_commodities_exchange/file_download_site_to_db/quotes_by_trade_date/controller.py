"""Controller for getting quotes for all products by trade date from the export site to and save to Database"""
from datetime import datetime, timedelta
from typing import Type, List, Optional

from app.core.controllers.file_download_site_to_db.datetime_based import DatetimeBasedFileDownloadSiteToDBController
from app.core.destinations.database.model import DatabaseBaseModel

from app.core.sources.file_download_site.datetime_based import DatetimeBasedFileDownloadSiteSource
from app.core.transformers.base import BaseTransformer
from app.core.transformers.empty_string_transformer import EmptyStringTransformer

from .destination.model import QuoteByTradeDate
from .source import QuotesByTradeDateDataset
from .transformers.datetime_transformers import QuotesUpdateDateTransformer, QuotesTradeDateTransformer, \
    QuotesUpdateTimeTransformer
from .transformers.field_value_alias_transformers import QuotesTradeTypeValueTransformer, \
    QuotesInstitutionsCodeValueTransformer, QuotesProductCodeValueTransformer


class ControllerForQuotesByTradeDate(DatetimeBasedFileDownloadSiteToDBController):
    """
    The controller for the quotes for all products by trade date resource
    got from the export site of the Tokyo Commodity Exchange
    """
    destination_model_class: Type[DatabaseBaseModel] = QuoteByTradeDate
    source_class: Type[DatetimeBasedFileDownloadSiteSource] = QuotesByTradeDateDataset
    interval_in_milliseconds: int = 20000
    start_datetime: Optional[datetime] = datetime.now().replace(minute=0) - timedelta(days=2)
    transformer_classes: List[Type[BaseTransformer]] = [
        EmptyStringTransformer,
        QuotesUpdateDateTransformer,
        QuotesTradeDateTransformer,
        QuotesUpdateTimeTransformer,
        QuotesTradeTypeValueTransformer,
        QuotesInstitutionsCodeValueTransformer,
        QuotesProductCodeValueTransformer,
    ]
