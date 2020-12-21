"""Module with the connection settings for the Blockchain.com historical service"""
import os

from judah.destinations.database.config import DatabaseConnectionConfig


class BlockchainHistoricalDbConnectionConfig(DatabaseConnectionConfig):
    db_uri: str = os.getenv("BLOCKCHAIN_HISTORICAL_DB_URI")
