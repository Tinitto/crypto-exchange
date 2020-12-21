"""Module containing configurations for the Finnhub database destination"""
from sqlalchemy.ext.declarative import declarative_base

from judah.destinations.database.model import DatabaseBaseModel

FinnhubLiveDBBase = declarative_base()


class FinnhubLiveDatabaseBaseModel(DatabaseBaseModel, FinnhubLiveDBBase):
    __abstract__ = True
    _base_declarative_class = FinnhubLiveDBBase
