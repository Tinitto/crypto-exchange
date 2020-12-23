"""Module containing all the controllers for the rest_api_to_db nomics service"""

from .currencies.controller import ControllerForCurrencies
from .currencies_ticker.controller import ControllerForCurrenciesTicker


NOMICS_REST_API_TO_DB_CONTROLLERS = [
    ControllerForCurrencies,
    ControllerForCurrenciesTicker,
]
