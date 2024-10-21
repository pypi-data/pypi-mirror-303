import os
from typing import Any
import sqlalchemy

class RdsDbConnection:
    _host: str
    _password: str
    _username: str
    _db_name: str
    _db_port: int
    _engine: sqlalchemy.Engine

    def __init__(self, create_engine: bool = True):
        self.load_config_from_env()

        if create_engine:
            self.create_engine()
    
    def create_engine(self):
        db_schema = "public"
        self._engine = sqlalchemy.create_engine(
            self._create_url(),
            connect_args={'options': '-csearch_path={}'.format(db_schema)})

    def load_config_from_env(self):
        self._host = os.getenv("DB_HOST")
        self._password = os.getenv("DB_PASSWORD")
        self._username = os.getenv("DB_USERNAME")
        self._db_name = os.getenv("DB_NAME")
        self._db_port = os.getenv("DB_PORT")
    
    def get_engine(self) -> sqlalchemy.Engine:
        return self._engine

    def _create_url(self) -> str:
        return f"postgresql://{self._username}:{self._password}@{self._host}:{self._db_port}/{self._db_name}"