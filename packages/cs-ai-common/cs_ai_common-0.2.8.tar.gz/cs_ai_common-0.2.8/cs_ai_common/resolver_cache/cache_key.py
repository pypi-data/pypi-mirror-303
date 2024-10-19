import hashlib


def build_cache_key(*args) -> str:
    return hashlib.md5(str(args).lower().encode()).hexdigest()

def build_s3_cache_key(hashed_key: str, resolver_name: str) -> str:
    return f"{hashed_key}/{resolver_name}/result.json"