"""The quotes for all products by session (day session) resource got from the export site"""
from app.core.utils.assets import FileOptions
from ..abstract.sources.index_based_source import TokyoCEIndexBasedFileDownloadSiteSource


class QuotesByDaySessionDataset(TokyoCEIndexBasedFileDownloadSiteSource):
    """
    Class for getting quotes for all products by day session data
    from the Tokyo Commodity Exchange export site
    """
    file_select_input_xpath: str = '//*[@id="article"]/form/table[3]/tbody/tr[2]/td[5]/select'
    download_button_xpath: str = '//*[@id="article"]/form/table[3]/tbody/tr[2]/td[5]/input'
    name: str = 'Quotes for all products by day session'
    file_options: FileOptions = FileOptions(xls_or_csv_headers=[
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
        "settlement_price",
        "volume",
        "irrelevant_column",
        "volume_total_by_products"
    ])
