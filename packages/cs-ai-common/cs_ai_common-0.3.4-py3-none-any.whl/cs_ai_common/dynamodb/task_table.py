import os
from cs_ai_common.dynamodb.utils import build_expression_attribute_names, build_expression_attribute_values, build_update_expression
from cs_ai_common.logging.internal_logger import InternalLogger
import boto3
from botocore.exceptions import ClientError


def update_task_status_failed(task_id: str) -> None:
    update_task(task_id, status="FAILED")
    
def update_task(task_id: str, **kwargs) -> None:
    dynamodb = boto3.client('dynamodb')
    table_name = os.getenv("TASKS_TABLE_NAME")
    try:
        dynamodb.update_item(
            TableName=table_name,
            Key={
                'task_id': {
                    'S': task_id
                }
            },
            UpdateExpression=build_update_expression(kwargs),
            ExpressionAttributeNames=build_expression_attribute_names(kwargs),
            ExpressionAttributeValues=build_expression_attribute_values(kwargs)
        )
        InternalLogger.LogDebug("UpdateItem succeeded")
    except ClientError as e:
        InternalLogger.LogError(f"Unable to update item: {e.response['Error']['Message']}")
        raise e

