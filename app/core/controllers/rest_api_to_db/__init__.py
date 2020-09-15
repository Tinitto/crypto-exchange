"""Module containing the controller class for getting data from the rest api to the database"""
from typing import Type

from ..base import BaseController
from app.core.destinations.database.model import DatabaseBaseModel
from app.core.sources.rest_api import RestAPISource


class RestAPIToDatabaseController(BaseController):
    """
    Class for the controller that gets data from the REST API
    and saves it in a database
    """
    _source: RestAPISource

    destination_model_class: Type[DatabaseBaseModel]
    source_class: Type[RestAPISource]
