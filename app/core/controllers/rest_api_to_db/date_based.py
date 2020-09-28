from datetime import date
from typing import Type, Optional

from app.core.controllers.base.date_based import DateBasedBaseController
from app.core.destinations.database.model import DatabaseBaseModel
from app.core.sources.rest_api.date_based import DateBasedRestAPISource
from app.core.utils.datetime import get_default_historical_start_date


class DateBasedRestAPIToDBController(DateBasedBaseController):
    """
    Class for the controller that gets data from a date-based REST API
    and saves it in a database
    """
    _source: DateBasedRestAPISource

    destination_model_class: Type[DatabaseBaseModel]
    source_class: Type[DateBasedRestAPISource]
    start_date: Optional[date] = get_default_historical_start_date()
