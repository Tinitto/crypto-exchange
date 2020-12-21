"""Module with the connection settings for the IEX historical service"""
import os

from judah.destinations.database.config import DatabaseConnectionConfig


class IEXHistoricalDbConnectionConfig(DatabaseConnectionConfig):
    db_uri: str = os.getenv("IEX_HISTORICAL_DB_URI")
