"""Module containing configurations for the Finnhub historical database destination"""
from sqlalchemy.ext.declarative import declarative_base

from judah.destinations.database.model import DatabaseBaseModel

FinnhubHistoricalDBBase = declarative_base()


class FinnhubHistoricalDatabaseBaseModel(DatabaseBaseModel, FinnhubHistoricalDBBase):
    __abstract__ = True
    _base_declarative_class = FinnhubHistoricalDBBase
