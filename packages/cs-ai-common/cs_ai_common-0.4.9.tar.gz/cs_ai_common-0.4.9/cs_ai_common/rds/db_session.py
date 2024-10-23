from cs_ai_common.rds.db_connection import RdsDbConnection
from sqlalchemy.orm import sessionmaker


class DbSession:
    _connection: RdsDbConnection

    def __init__(self, connection: RdsDbConnection):
        self._connection = connection

    def get_session(self):
        engine = self._connection.get_engine()
        Session = sessionmaker(bind=engine)
        return Session()
