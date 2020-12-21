"""Module with the connection settings for the Nomics service"""
import os

from judah.destinations.database.config import DatabaseConnectionConfig


class NomicsDbConnectionConfig(DatabaseConnectionConfig):
    db_uri: str = os.getenv("NOMICS_LIVE_DB_URI")
