"""Module with the connection settings for the Blockchain service"""
import os

from app.core.destinations.database.config import DatabaseConnectionConfig


class BlockchainLiveDbConnectionConfig(DatabaseConnectionConfig):
    db_uri: str = os.getenv("BLOCKCHAIN_LIVE_DB_URI")
