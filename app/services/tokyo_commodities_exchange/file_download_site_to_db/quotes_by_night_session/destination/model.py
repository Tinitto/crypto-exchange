"""Model for quotes for all products by night session"""
import sqlalchemy as orm

from ...abstract.destinations.tokyo_c_e_historical_db import TokyoCEHistoricalDBBaseModel, \
    TokyoCEHistoricalDbConnectionConfig


class QuoteByNightSession(TokyoCEHistoricalDBBaseModel):
    """
    Database model for "Quotes for All Products by Session (Night Session)"
    """
    __tablename__ = 'quotes_by_night_session'
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
    irrelevant_column = orm.Column(orm.Text)
    settlement_price = orm.Column(orm.FLOAT(precision=15, decimal_return_scale=2))
    volume = orm.Column(orm.FLOAT(precision=15, decimal_return_scale=2))
    volume_total_by_products = orm.Column(orm.FLOAT(precision=15, decimal_return_scale=2))
