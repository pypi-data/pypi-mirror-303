import json
import os
import boto3
from cs_ai_common.s3.utils import get_bucket_name_from_arn


BUCKET_NAME = get_bucket_name_from_arn(os.getenv("RESULTS_BUCKET_NAME", None))

def write_result_to_s3(result: dict, key: str, bucket_name: str | None = None) -> None:
    s3 = boto3.client('s3')
    object_key = key
    _bucket_name = bucket_name if bucket_name is not None else BUCKET_NAME
    response = s3.put_object(
        Body=json.dumps(result),
        Bucket=_bucket_name,
        Key=object_key
    )
    return response