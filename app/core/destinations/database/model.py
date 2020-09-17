"""Base class for models"""
import logging
from typing import Dict, Any, Type, List

from sqlalchemy import inspect, and_, or_, Column, DateTime, schema, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, ProgrammingError
from sqlalchemy.sql import func

from ..base import DestinationBaseModel
from app.core.destinations.database.config import DatabaseConnectionConfig
from app.core.destinations.database.connection import DatabaseConnection


class DatabaseBaseModel(DestinationBaseModel):
    __abstract__: bool = True
    __table_args__: Dict = {}
    __table__: Any
    _db_configuration: DatabaseConnectionConfig
    _base_declarative_class: Type[declarative_base()]
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    @classmethod
    def get_attributes(cls) -> List[str]:
        return cls.__table__.columns.keys()

    def update(self, session: Session, **kwargs):
        """
        Updates the attributes passed in the kwargs and saves
        """
        for key, word in kwargs.items():
            self.__setattr__(key, word)
        self.save(session)

        return self

    def save(self, session: Session):
        """Commits changes to the database"""
        session.add(self)
        session.commit()

    def delete(self, session: Session, ):
        """Deletes the current record"""
        session.delete(self)
        session.commit()

    @classmethod
    def create_schema(cls, db_engine: engine.Engine):
        """Create the schema for this class if it exists"""
        schema_name = cls.__table_args__.get('schema', None)

        if schema_name is not None:
            try:
                db_engine.execute(schema.CreateSchema(schema_name))
            except (IntegrityError, ProgrammingError,):
                pass

    @classmethod
    def initialize(cls):
        """Creates the tables in the database"""
        with DatabaseConnection.get_db_connection(
                db_connection_config=cls._db_configuration) as db_connection:
            try:
                db_engine = db_connection.connection_engine

                cls.create_schema(db_engine=db_engine)

                cls._base_declarative_class.metadata.create_all(bind=db_engine)
            except (IntegrityError, ProgrammingError) as exp:
                logging.info(f"{cls.__table__} already created. \n{exp}")

    @classmethod
    def upsert(cls, data: Dict[Any, Any]):
        """
        Updates the given record row or creates it if it does not exist
        Returns data so that it can be used by the next pipe
        """
        with DatabaseConnection.get_db_connection(
                db_connection_config=cls._db_configuration) as db_connection:
            session = db_connection.db_session

            primary_key_columns = [column for column in inspect(cls).primary_key]
            is_data_with_primary_key = any([column.key in data for column in primary_key_columns])

            if is_data_with_primary_key:
                record = session.query(cls).filter(
                    or_(and_(*(column == data[column.key] for column in primary_key_columns)))
                ).first()

                if record:
                    record.update(session=session, **data)
                    return data

            record = cls(**data)
            record.save(session)
            return data

