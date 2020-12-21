"""Module containing configurations for the Blockchain live database destination"""
from sqlalchemy.ext.declarative import declarative_base

from judah.destinations.database.model import DatabaseBaseModel

BlockchainLiveDBBase = declarative_base()


class BlockchainLiveDatabaseBaseModel(DatabaseBaseModel, BlockchainLiveDBBase):
    __abstract__ = True
    _base_declarative_class = BlockchainLiveDBBase
