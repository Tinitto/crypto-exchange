"""Module containing all the controllers for the file_download_site_to_db nomics service"""

from .quotes_by_trade_date import ControllerForQuotesByTradeDate
from .quotes_by_day_session import ControllerForQuotesByDaySession
from .quotes_by_night_session import ControllerForQuotesByNightSession

TOKYO_C_E_FILE_DOWNLOAD_SITE_TO_DB_CONTROLLERS = [
    ControllerForQuotesByTradeDate,
    ControllerForQuotesByDaySession,
    ControllerForQuotesByNightSession,
]
