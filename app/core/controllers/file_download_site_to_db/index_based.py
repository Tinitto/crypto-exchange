from datetime import datetime
from typing import Type, Optional

from app.core.controllers.base import BaseController
from app.core.destinations.database.model import DatabaseBaseModel
from app.core.sources.file_download_site.index_based import IndexBasedFileDownloadSiteSource
from app.core.utils.datetime import get_default_historical_start_datetime


class IndexBasedFileDownloadSiteToDBController(BaseController):
    """
    Class for the controller that downloads data from a index-based export site
    and saves it in a database
    """
    _source: IndexBasedFileDownloadSiteSource

    destination_model_class: Type[DatabaseBaseModel]
    source_class: Type[IndexBasedFileDownloadSiteSource]
