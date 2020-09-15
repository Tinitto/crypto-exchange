"""Module containing configurations for the nomics database destination"""
from sqlalchemy.ext.declarative import declarative_base

from app.core.destinations.database.model import DatabaseBaseModel

NomicsLiveDBBase = declarative_base()


class NomicsDatabaseBaseModel(DatabaseBaseModel, NomicsLiveDBBase):
    __abstract__ = True
    _base_declarative_class = NomicsLiveDBBase
