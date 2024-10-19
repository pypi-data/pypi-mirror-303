from contextlib import (
    suppress,
)
import diskcache
from diskcache import (
    Lock,
)
import diskcache.core
import functools
import hashlib
import os
import pickle
from platformdirs import (
    user_cache_dir,
)
import redis
import socket
from typing import (
    Any,
    Callable,
    cast,
    TypeVar,
)

REDIS_CACHE_ENDPOINT = os.environ.get("CACHE_URL")
REDIS_CLIENT = None

TVar = TypeVar("TVar")  # pylint: disable=invalid-name
TFun = TypeVar(  # pylint: disable=invalid-name
    "TFun", bound=Callable[..., Any]
)

if REDIS_CACHE_ENDPOINT:
    try:
        host, _port = REDIS_CACHE_ENDPOINT.split(":", maxsplit=1)
        port = int(_port)

        # Intentar conectarse al endpoint de Redis
        socket.create_connection((host, port), timeout=2)

        REDIS_CLIENT = redis.StrictRedis(
            host=host,
            port=port,
            ssl=True,
            username="readwrite",
            password=os.environ.get("CACHE_USER_WRITE_PASSWORD"),
        )
    except (socket.error, ValueError):
        REDIS_CLIENT = None

DISK_CACHE = diskcache.Cache(user_cache_dir("fluid-sbom", "fluidattacks"))


# 4 weeks
TTL = 604800 * 4


def make_hashable(item: Any) -> str:
    serialized_object = pickle.dumps(item)

    return hashlib.sha256(serialized_object).hexdigest()


def generate_cache_key(func: Any, args: Any, kwargs: dict[Any, Any]) -> str:
    key = f"{func.__module__}.{func.__name__}-"
    key += str(make_hashable((args, kwargs)))
    return hashlib.sha256(key.encode()).hexdigest()


def dual_cache(func: TVar) -> TVar:
    _func = cast(Callable[..., Any], func)

    @functools.wraps(_func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_key = generate_cache_key(_func, args, kwargs)

        # Try to recover from disk cache
        if value := DISK_CACHE.get(cache_key):
            return value
        # Try to recover from Redis cache (ElastiCache) if available
        if REDIS_CLIENT:
            cached_result = REDIS_CLIENT.get(cache_key)

            if cached_result:
                result = pickle.loads(cached_result)  # type: ignore
                with Lock(DISK_CACHE, "dual_cache"):
                    DISK_CACHE.set(
                        cache_key, result, expire=TTL, retry=True
                    )  # Save to disk with TTL

                return result

        # Run the function and store the result in both caches
        result = _func(*args, **kwargs)
        with suppress(diskcache.core.Timeout):
            with Lock(DISK_CACHE, "dual_cache"):
                DISK_CACHE.set(
                    cache_key, result, expire=TTL, retry=True
                )  # Save to disk with TTL
        if REDIS_CLIENT:
            REDIS_CLIENT.setex(
                cache_key, TTL, pickle.dumps(result)
            )  # Save to Redis with TTL
        return result

    return cast(TVar, wrapper)
