"""Module containing the controller class for getting data from the rest api to the database without paginating"""
from typing import Type

from judah.controllers.base import BaseController
from judah.destinations.database.model import DatabaseBaseModel

from ..sources.bulk import NomicsBulkRestApiSource


class NomicsBulkRestAPIToDatabaseController(BaseController):
    """
    Class for the controller that gets data in one chunk from the REST API
    and saves it in a database without paginating through the list of records in the source
    """
    _source: NomicsBulkRestApiSource

    destination_model_class: Type[DatabaseBaseModel]
    source_class: Type[NomicsBulkRestApiSource]
