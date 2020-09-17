from typing import Type

from app.core.controllers.base.date_based import DateBasedBaseController
from app.core.destinations.database.model import DatabaseBaseModel
from app.core.sources.rest_api.date_based import DateBasedRestAPISource


class DateBasedRestAPIToDBController(DateBasedBaseController):
    """
    Class for the controller that gets data from a date-based REST API
    and saves it in a database
    """
    _source: DateBasedRestAPISource

    destination_model_class: Type[DatabaseBaseModel]
    source_class: Type[DateBasedRestAPISource]
