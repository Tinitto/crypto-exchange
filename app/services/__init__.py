"""Entry point for all services"""

from .nomics.rest_api_to_db import NOMICS_REST_API_TO_DB_CONTROLLERS
from .tokyo_commodities_exchange.export_site_to_db import TOKYO_C_E_EXPORT_SITE_TO_DB_CONTROLLERS
from .blockchain.rest_api_to_db import BLOCKCHAIN_REST_API_TO_DB_CONTROLLERS
from .finnhub.rest_api_to_db import FINNHUB_REST_API_TO_DB_CONTROLLERS
from .iex.rest_api_to_db import IEX_REST_API_TO_DB_CONTROLLERS

ALL_SERVICE_CONTROLLERS = (
        NOMICS_REST_API_TO_DB_CONTROLLERS +
        TOKYO_C_E_EXPORT_SITE_TO_DB_CONTROLLERS +
        BLOCKCHAIN_REST_API_TO_DB_CONTROLLERS +
        FINNHUB_REST_API_TO_DB_CONTROLLERS +
        IEX_REST_API_TO_DB_CONTROLLERS)
