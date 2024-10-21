from cs_ai_common.rds.db_connection import RdsDbConnection
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_db_schema() -> None:
    rds_db_connection = RdsDbConnection()
    engine = rds_db_connection.get_engine()
    Base.metadata.create_all(engine)