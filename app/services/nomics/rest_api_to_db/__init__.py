"""Module containing all the controllers for the rest_api_to_db nomics service"""

from .currencies.controller import ControllerForCurrencies


NOMICS_REST_API_TO_DB_CONTROLLERS = [
    ControllerForCurrencies,
]
