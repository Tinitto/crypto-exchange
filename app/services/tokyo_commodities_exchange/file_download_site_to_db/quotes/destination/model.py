"""Model for quotes for all products by trade date"""
import uuid

import sqlalchemy as orm
from sqlalchemy.dialects.postgresql import UUID

from ...abstract.destinations.tokyo_c_e_historical_db import TokyoCEHistoricalDBBaseModel, \
    TokyoCEHistoricalDbConnectionConfig


class Quote(TokyoCEHistoricalDBBaseModel):
    """
    Database model for "Quotes for All Products by Trade Date"
    """
    __tablename__ = 'quotes'
    _db_configuration = TokyoCEHistoricalDbConnectionConfig()

    _id = orm.Column(UUID(as_uuid=True), name='id', primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    update_date = orm.Column(orm.Date)
    update_time = orm.Column(orm.Time)
    trade_date = orm.Column(orm.Date)
    institutions_code = orm.Column(orm.VARCHAR(10))
    trade_type = orm.Column(orm.VARCHAR(255))
    product_code = orm.Column(orm.Text)
    contract_month = orm.Column(orm.VARCHAR(20))
    strike_price = orm.Column(orm.Integer)
    at_the_money_flag = orm.Column(orm.VARCHAR(10))
    volume_fix_flag = orm.Column(orm.VARCHAR(10))
    settlement_flag = orm.Column(orm.VARCHAR(10))
    session_end_flag = orm.Column(orm.VARCHAR(10))
    start_price = orm.Column(orm.Integer)
    high_price = orm.Column(orm.Integer)
    low_price = orm.Column(orm.Integer)
    current_price = orm.Column(orm.Integer)
    last_settlement_price = orm.Column(orm.Integer)
    offset_from_previous_day = orm.Column(orm.Integer)
    percent_offset_from_previous_day = orm.Column(orm.FLOAT(precision=15, decimal_return_scale=2))
    irrelevant_column = orm.Column(orm.Text)
    settlement_price = orm.Column(orm.Integer)
    volume = orm.Column(orm.Integer)
    volume_total_by_products = orm.Column(orm.Integer)
