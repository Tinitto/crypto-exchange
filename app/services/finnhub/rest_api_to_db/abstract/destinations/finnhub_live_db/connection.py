"""Module with the connection settings for the Finnhub Live service"""
import os

from app.core.destinations.database.config import DatabaseConnectionConfig


class FinnhubLiveDbConnectionConfig(DatabaseConnectionConfig):
    db_uri: str = os.getenv("FINNHUB_LIVE_DB_URI")
