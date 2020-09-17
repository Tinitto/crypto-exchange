"""Module containing configurations for the tokyo_c_e historical database destination"""
from sqlalchemy.ext.declarative import declarative_base

from app.core.destinations.database.model import DatabaseBaseModel

TokyoCEHistoricalDBBase = declarative_base()


class TokyoCEHistoricalDBBaseModel(DatabaseBaseModel, TokyoCEHistoricalDBBase):
    __abstract__ = True
    _base_declarative_class = TokyoCEHistoricalDBBase
    __table_args__ = {'schema': 'downloads'}
