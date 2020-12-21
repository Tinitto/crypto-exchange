"""Module with the connection settings for the Finnhub Historical service"""
import os

from judah.destinations.database.config import DatabaseConnectionConfig


class FinnhubHistoricalDbConnectionConfig(DatabaseConnectionConfig):
    db_uri: str = os.getenv("FINNHUB_HISTORICAL_DB_URI")
