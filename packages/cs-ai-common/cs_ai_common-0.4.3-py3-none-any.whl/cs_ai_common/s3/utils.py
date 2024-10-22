import json
from typing import Dict, Optional
import boto3
from botocore.exceptions import ClientError

def try_get_object(key: str, bucket: str) -> Optional[Dict]:
    try:
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=bucket, Key=key)
        return json.loads(response["Body"].read().decode("utf-8"))
    except ClientError as e:
        if e.response["Error"]["Code"] == "NoSuchKey":
            return None
        raise e
    
def get_bucket_name_from_arn(arn: str) -> str:
    return arn[13:] if arn is not None else None