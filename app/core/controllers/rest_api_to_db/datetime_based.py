from datetime import datetime
from typing import Type, Optional

from app.core.controllers.base.datetime_based import DatetimeBasedBaseController
from app.core.destinations.database.model import DatabaseBaseModel
from app.core.sources.rest_api.datetime_based import DatetimeBasedRestAPISource
from app.core.utils.datetime import get_default_historical_start_datetime


class DatetimeBasedRestAPIToDBController(DatetimeBasedBaseController):
    """
    Class for the controller that gets data from a datetime-based REST API
    and saves it in a database
    """
    _source: DatetimeBasedRestAPISource

    destination_model_class: Type[DatabaseBaseModel]
    source_class: Type[DatetimeBasedRestAPISource]
    start_datetime: Optional[datetime] = get_default_historical_start_datetime()
