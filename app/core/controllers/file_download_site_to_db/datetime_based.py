from datetime import datetime
from typing import Type, Optional

from app.core.controllers.base.datetime_based import DatetimeBasedBaseController
from app.core.destinations.database.model import DatabaseBaseModel
from app.core.sources.file_download_site.datetime_based import DatetimeBasedFileDownloadSiteSource
from app.core.utils.datetime import get_default_historical_start_datetime


class DatetimeBasedFileDownloadSiteToDBController(DatetimeBasedBaseController):
    """
    Class for the controller that downloads data from a datetime-based export site
    and saves it in a database
    """
    _source: DatetimeBasedFileDownloadSiteSource

    destination_model_class: Type[DatabaseBaseModel]
    source_class: Type[DatetimeBasedFileDownloadSiteSource]
    start_datetime: Optional[datetime] = get_default_historical_start_datetime()
