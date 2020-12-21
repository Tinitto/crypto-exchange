"""Module containing configurations for the IEX live database destination"""
from sqlalchemy.ext.declarative import declarative_base

from judah.destinations.database.model import DatabaseBaseModel

IEXHistoricalDBBase = declarative_base()


class IEXHistoricalDatabaseBaseModel(DatabaseBaseModel, IEXHistoricalDBBase):
    __abstract__ = True
    _base_declarative_class = IEXHistoricalDBBase
