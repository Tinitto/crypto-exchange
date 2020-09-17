"""Module with the connection settings for the IEX service"""
import os

from app.core.destinations.database.config import DatabaseConnectionConfig


class IEXLiveDbConnectionConfig(DatabaseConnectionConfig):
    db_uri: str = os.getenv("IEX_LIVE_DB_URI")
