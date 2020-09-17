"""Module with the connection settings for the Blockchain.com historical service"""
import os

from app.core.destinations.database.config import DatabaseConnectionConfig


class BlockchainHistoricalDbConnectionConfig(DatabaseConnectionConfig):
    db_uri: str = os.getenv("BLOCKCHAIN_HISTORICAL_DB_URI")
