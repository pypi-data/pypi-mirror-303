from typing import Dict, Optional

from cs_ai_common.resolver_cache.cache_key import build_s3_cache_key
from cs_ai_common.s3.resolver_results import write_result_to_s3
from cs_ai_common.s3.utils import try_get_object


def try_get_cached_result(cache_key: str, resolver_name: str, bucket_name: str) -> Dict | None:
    return try_get_object(build_s3_cache_key(cache_key, resolver_name), bucket_name)

def save_cache_result(cache_key: str, resolver_name: str, result: Dict, bucket_name: str) -> None:
    cache_key = build_s3_cache_key(cache_key, resolver_name)
    write_result_to_s3(result, cache_key, bucket_name)