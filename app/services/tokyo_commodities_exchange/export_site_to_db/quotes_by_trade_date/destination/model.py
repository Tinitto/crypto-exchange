"""Model for quotes for all products by trade date"""
import sqlalchemy as orm

from ...abstract.destinations.tokyo_c_e_historical_db import TokyoCEHistoricalDBBaseModel, \
    TokyoCEHistoricalDbConnectionConfig


class QuoteByTradeDate(TokyoCEHistoricalDBBaseModel):
    """
    Database model for "Quotes for All Products by Trade Date"
    """
    __tablename__ = 'quotes_by_trade_date'
    _db_configuration = TokyoCEHistoricalDbConnectionConfig()

    update_date = orm.Column(orm.Date, primary_key=True)
    update_time = orm.Column(orm.Time, primary_key=True)
    trade_date = orm.Column(orm.Date, primary_key=True)
    institutions_code = orm.Column(orm.VARCHAR(10))
    trade_type = orm.Column(orm.VARCHAR(255))
    product_code = orm.Column(orm.Text, primary_key=True)
    contract_month = orm.Column(orm.VARCHAR(20), primary_key=True)
    strike_price = orm.Column(orm.FLOAT(precision=15, decimal_return_scale=2))
    at_the_money_flag = orm.Column(orm.VARCHAR(10))
    volume_fix_flag = orm.Column(orm.VARCHAR(10))
    settlement_flag = orm.Column(orm.VARCHAR(10))
    session_end_flag = orm.Column(orm.VARCHAR(10))
    start_price = orm.Column(orm.FLOAT(precision=15, decimal_return_scale=2))
    high_price = orm.Column(orm.FLOAT(precision=15, decimal_return_scale=2))
    low_price = orm.Column(orm.FLOAT(precision=15, decimal_return_scale=2))
    current_price = orm.Column(orm.FLOAT(precision=15, decimal_return_scale=2))
    last_settlement_price = orm.Column(orm.FLOAT(precision=15, decimal_return_scale=2))
    offset_from_previous_day = orm.Column(orm.FLOAT(precision=15, decimal_return_scale=2))
    percent_offset_from_previous_day = orm.Column(orm.FLOAT(precision=15, decimal_return_scale=2))
    irrelevant_column = orm.Column(orm.Text)
    settlement_price = orm.Column(orm.FLOAT(precision=15, decimal_return_scale=2))
    volume = orm.Column(orm.FLOAT(precision=15, decimal_return_scale=2))
    volume_total_by_products = orm.Column(orm.FLOAT(precision=15, decimal_return_scale=2))
