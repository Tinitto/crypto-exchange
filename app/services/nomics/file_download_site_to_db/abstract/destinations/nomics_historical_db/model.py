"""Module containing configurations for the nomics database destination"""
from sqlalchemy.ext.declarative import declarative_base

from app.core.destinations.database.model import DatabaseBaseModel

NomicsHistoricalDBBase = declarative_base()


class NomicsHistoricalDBBaseModel(DatabaseBaseModel, NomicsHistoricalDBBase):
    __abstract__ = True
    _base_declarative_class = NomicsHistoricalDBBase
    __table_args__ = {'schema': 'file_download_data'}
