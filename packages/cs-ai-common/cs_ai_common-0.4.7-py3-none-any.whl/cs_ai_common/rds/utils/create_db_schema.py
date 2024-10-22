from cs_ai_common.logging.internal_logger import InternalLogger
from cs_ai_common.rds.db_connection import RdsDbConnection
from cs_ai_common.rds.entities.base import Base

def create_db_schema() -> None:
    InternalLogger.LogDebug("Creating database schema")
    InternalLogger.LogDebug(f"Creating tables: {Base.metadata.tables.keys()}")
    rds_db_connection = RdsDbConnection()
    engine = rds_db_connection.get_engine()
    Base.metadata.create_all(engine)