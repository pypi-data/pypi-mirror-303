from cs_ai_common.dynamodb.task_table import update_task_status_failed
from cs_ai_common.logging.internal_logger import InternalLogger


def startup_app(callback, retry_on, retries: int, raw_event: dict = None):
    try:
        return callback()
    except retry_on as e:
        InternalLogger.LogDebug(f"Attenpting to retry {callback.__name__} due to {e}")
        if retries > 0:
            InternalLogger.LogDebug(f"Retrying {callback.__name__} due to {e}")
            return startup_app(callback, retry_on=retry_on, retries=retries - 1, raw_event=raw_event)
        else:
            InternalLogger.LogError(f"Failed to run {callback.__name__} after retries. Last error: {e}")
            _update_task_status_failed(raw_event)
            raise                                               
    except Exception as e:
        InternalLogger.LogError(f"Failed to run {callback.__name__}. Error: {e}")
        _update_task_status_failed(raw_event)
        raise e
        
def _update_task_status_failed(raw_event: dict):
    task_id = raw_event["task_id"]
    update_task_status_failed(task_id)