"""Module containing the controller class for getting data from the rest api to the database with paginating"""
from typing import Type

from judah.controllers.base import BaseController
from judah.destinations.database.model import DatabaseBaseModel

from ..sources.paginated import NomicsPaginatedRestApiSource


class NomicsPaginatedRestAPIToDatabaseController(BaseController):
    """
    Class for the controller that gets data from the REST API with pagination
    and saves it in a database
    """
    _source: NomicsPaginatedRestApiSource

    destination_model_class: Type[DatabaseBaseModel]
    source_class: Type[NomicsPaginatedRestApiSource]
