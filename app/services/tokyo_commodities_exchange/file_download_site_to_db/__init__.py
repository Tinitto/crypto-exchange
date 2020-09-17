"""Module containing all the controllers for the file_download_site_to_db nomics service"""

from .quotes_by_trade_date import ControllerForQuotesByTradeDate

TOKYO_C_E_FILE_DOWNLOAD_SITE_TO_DB_CONTROLLERS = [
    ControllerForQuotesByTradeDate,
]
