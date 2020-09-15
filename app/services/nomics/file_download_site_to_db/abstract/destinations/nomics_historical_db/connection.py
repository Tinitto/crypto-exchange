"""Module with the connection settings for the Netherlands historical service"""
import os

from app.core.destinations.database.config import DatabaseConnectionConfig


class NomicsHistoricalDbConnectionConfig(DatabaseConnectionConfig):
    db_uri: str = os.getenv("NOMICS_HISTORICAL_DB_URI")
