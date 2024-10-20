from flask import Flask
from logging import INFO, DEBUG

from flask_sqlalchemy.model import Model
from sqlalchemy import Engine, text, MetaData
from sqlalchemy.ext.declarative import declarative_base as _declarative_base
from sqlalchemy.orm import sessionmaker


class DBCareEngine:
    def __init__(self, db_engine: Engine, declarative_base: Model = None, flask_app: Flask = None):
        self.base = declarative_base or _declarative_base()
        self.engine = db_engine
        self.__flask_app = flask_app

    def __enter__(self):
        self.session = sessionmaker(bind=self.engine)()
        self.connection = self.engine.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        self.session.close()
        return False

    def _log(self, message, level=INFO):
        if self.__flask_app:
            self.__flask_app.logger.log(level, message)

    def find_models(self) -> list:
        models = list()

        def find_subclasses(cls):
            for subclass in cls.__subclasses__():
                find_subclasses(subclass)
                models.append(subclass)

        find_subclasses(self.base)
        return models

    def find_tables(self) -> dict:
        metadata = MetaData()
        metadata.reflect(bind=self.engine)
        return metadata.tables

    def _fix_missing_columns(self, model, missing_columns):
        for column in missing_columns:
            column = model.__table__.columns.get(column)

            column_definition = f'{column.name} {column.type.compile(dialect=self.engine.dialect)}'
            alter_table_sql = f'ALTER TABLE {model.__tablename__} ADD COLUMN {column_definition}'
            self.connection.execute(text(alter_table_sql))

            self._log(f"Column '{column.name}' added to '{model.__tablename__}'")

    def _fix_extra_columns(self, model, extra_columns):
        for column in extra_columns:
            self.connection.execute(text(
                f"ALTER TABLE {model.__tablename__} DROP COLUMN {column}"
            ))

            self._log(f"Column '{column}' dropped from '{model.__tablename__}'")

    def treat_tables(self):
        all_models = self.find_models()
        all_tables = self.find_tables()

        for model in all_models:
            if not hasattr(model, "__tablename__"):
                self._log(f"Table '{model.__name__}' has no name. Might be abstract. Skipping...", DEBUG)
                continue
            elif model.__tablename__ not in all_tables:
                self._log(f"Table '{model.__tablename__}' not found in database. Skipping...", DEBUG)
                continue

            table = all_tables.get(model.__tablename__)
            model_columns = model.__table__.columns.keys()
            existing_columns = table.columns.keys()

            missing_columns = set(model_columns) - set(existing_columns)
            extra_columns = set(existing_columns) - set(model_columns)

            self._log(f"Missing columns for '{model.__tablename__}': {missing_columns}", DEBUG)
            self._log(f"Extra columns for '{model.__tablename__}': {extra_columns}", DEBUG)

            if missing_columns:
                self._fix_missing_columns(model, missing_columns)

            if extra_columns:
                self._fix_extra_columns(model, extra_columns)

    def run_custom_task(self, task: callable):
        task(self)
