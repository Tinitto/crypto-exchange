"""The quotes for all products by trade date resource got from the export site"""
from typing import List

from ..abstract.sources.datetime_based_source import TokyoCEDatetimeBasedFileDownloadSiteSource


class QuotesDataset(TokyoCEDatetimeBasedFileDownloadSiteSource):
    """Class for getting quotes for all products data from the Tokyo Commodity Exchange export site"""
    start_datetime_select_input_xpath: str = '//*[@id="article"]/form/table[3]/tbody/tr[1]/td[5]/select'
    download_button_xpath: str = '//*[@id="article"]/form/table[3]/tbody/tr[1]/td[5]/input'
    name: str = 'Quotes for all products by trade date'
    default_batch_size_in_milliseconds: int = 5 * 60 * 1000  # 5 minutes
    file_prefix: str = 'souba_d_'
    headers: List[str] = [
        "update_date",
        "update_time",
        "trade_date",
        "institutions_code",
        "trade_type",
        "product_code",
        "contract_month",
        "strike_price",
        "at_the_money_flag",
        "volume_fix_flag",
        "settlement_flag",
        "session_end_flag",
        "start_price",
        "high_price",
        "low_price",
        "current_price",
        "last_settlement_price",
        "offset_from_previous_day",
        "percent_offset_from_previous_day",
        "irrelevant_column",
        "settlement_price",
        "volume",
        "volume_total_by_products"
    ]
