from typing import Type

from app.core.controllers.base.datetime_based import DatetimeBasedBaseController
from app.core.destinations.database.model import DatabaseBaseModel
from app.core.sources.file_download_site.datetime_based import DatetimeBasedFileDownloadSiteSource


class DatetimeBasedFileDownloadSiteToDBController(DatetimeBasedBaseController):
    """
    Class for the controller that downloads data from a datetime-based export site
    and saves it in a database
    """
    _source: DatetimeBasedFileDownloadSiteSource

    destination_model_class: Type[DatabaseBaseModel]
    source_class: Type[DatetimeBasedFileDownloadSiteSource]
