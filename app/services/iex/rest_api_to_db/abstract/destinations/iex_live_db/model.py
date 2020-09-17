"""Module containing configurations for the IEX live database destination"""
from sqlalchemy.ext.declarative import declarative_base

from app.core.destinations.database.model import DatabaseBaseModel

IEXLiveDBBase = declarative_base()


class IEXLiveDatabaseBaseModel(DatabaseBaseModel, IEXLiveDBBase):
    __abstract__ = True
    _base_declarative_class = IEXLiveDBBase
