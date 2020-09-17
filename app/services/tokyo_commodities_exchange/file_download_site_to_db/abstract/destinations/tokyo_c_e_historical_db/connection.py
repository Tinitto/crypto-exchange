"""Module with the connection settings for the Tokyo Commodities Exchange file download service"""
import os

from app.core.destinations.database.config import DatabaseConnectionConfig


class TokyoCEHistoricalDbConnectionConfig(DatabaseConnectionConfig):
    db_uri: str = os.getenv("TOKYO_COMMODITIES_HISTORICAL_DB_URI")
