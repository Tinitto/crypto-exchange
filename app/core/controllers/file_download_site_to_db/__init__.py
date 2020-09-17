"""Module containing the controller class for getting data from the export site to the database"""
from typing import Type

from ..base import BaseController
from app.core.destinations.database.model import DatabaseBaseModel
from app.core.sources.file_download_site import FileDownloadSiteSource


class FileDownloadSiteToDatabaseController(BaseController):
    """
    Class for the controller that downloads data from the export site
    and saves it in a database
    """
    _source: FileDownloadSiteSource

    destination_model_class: Type[DatabaseBaseModel]
    source_class: Type[FileDownloadSiteSource]


