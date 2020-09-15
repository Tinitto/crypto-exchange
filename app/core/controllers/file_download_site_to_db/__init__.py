"""Module containing the controller class for getting data from the export site to the database"""
from datetime import date
from typing import Type, Optional

from ..base import BaseController
from app.core.destinations.database.model import DatabaseBaseModel
from app.core.sources.file_download_site import FileDownloadSiteSource
from ...utils.dates import get_default_historical_start_date


class FileDownloadSiteToDatabaseController(BaseController):
    """
    Class for the controller that downloads data from the export site
    and saves it in a database
    """
    _source: FileDownloadSiteSource

    destination_model_class: Type[DatabaseBaseModel]
    source_class: Type[FileDownloadSiteSource]
    start_date: Optional[date] = get_default_historical_start_date()
