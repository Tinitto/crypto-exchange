from datetime import date
from typing import Type, Optional

from app.core.controllers.base.date_based import DateBasedBaseController
from app.core.destinations.database.model import DatabaseBaseModel
from app.core.sources.file_download_site.date_based import DateBasedFileDownloadSiteSource
from app.core.utils.datetime import get_default_historical_start_date


class DateBasedFileDownloadSiteToDBController(DateBasedBaseController):
    """
    Class for the controller that downloads data from a date-based export site
    and saves it in a database
    """
    _source: DateBasedFileDownloadSiteSource

    destination_model_class: Type[DatabaseBaseModel]
    source_class: Type[DateBasedFileDownloadSiteSource]
    start_date: Optional[date] = get_default_historical_start_date()
