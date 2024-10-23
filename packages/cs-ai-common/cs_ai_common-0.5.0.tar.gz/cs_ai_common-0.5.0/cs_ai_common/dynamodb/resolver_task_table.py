from cs_ai_common.dynamodb.utils import build_expression_attribute_names, build_expression_attribute_values, build_update_expression
from botocore.exceptions import ClientError
import boto3
import os
from cs_ai_common.logging.internal_logger import InternalLogger

def update_resolver_task(task_id: str, resolver_name: str, **kwargs) -> None:
    dynamodb = boto3.client('dynamodb')
    table_name = os.getenv("RESULTS_TABLE_NAME")
    try:
        _update_expression = build_update_expression(kwargs)
        _expression_attribute_names = build_expression_attribute_names(kwargs)
        _expression_attribute_values = build_expression_attribute_values(kwargs)    
        InternalLogger.LogDebug(f"UpdateItem: {table_name}, {task_id}, {resolver_name}, {_update_expression}, {_expression_attribute_names}, {_expression_attribute_values}")
        dynamodb.update_item(
            TableName=table_name,
            Key={
                'task_id': {
                    'S': task_id
                },
                'resolver': {
                    'S': resolver_name
                }
            },
            UpdateExpression=_update_expression,
            ExpressionAttributeNames=_expression_attribute_names,
            ExpressionAttributeValues=_expression_attribute_values
        )
        InternalLogger.LogDebug("UpdateItem succeeded")
    except ClientError as e:
        InternalLogger.LogError(f"Unable to update item: {e.response['Error']['Message']}")
        raise e
    
def insert_resolver_result_task(task_id: str, resolver_name: str, **kwargs) -> None:
    RESULTS_TABLE_NAME = os.getenv("RESULTS_TABLE_NAME", "")
    dynamodb = boto3.client('dynamodb')
    item = {
        'task_id': {
            'S': task_id
        },
        'resolver': {
            'S': resolver_name
        },
    }

    for key, value in kwargs.items():
        item[key] = {
            'S': value
        }

    dynamodb.put_item(TableName=RESULTS_TABLE_NAME, Item=item)