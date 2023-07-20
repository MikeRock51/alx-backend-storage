#!/usr/bin/env python3
"""Exploring Redis basics/ Redis-py"""

import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Keeps track of how often the Cache class methods are called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increments the key"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Caching with Redis"""

    rTypes = Union[str, bytes, int, float]

    def __init__(self):
        """Stores a Redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: rTypes) -> str:
        """Stores data in redis and returns the ID"""

        id: str = str(uuid4())
        self._redis.set(id, data)

        return id

    def get(self, key: str, fn: Optional[Callable] = None) -> rTypes:
        """Retrieves key from redis in the requested format"""

        if not fn:
            return self._redis.get(key)
        return fn(self._redis.get(key))

    def get_str(self, key: str) -> str:
        """
            Automatically parametrize Cache.get
            with the correct conversion function.
        """
        return self._redis.get(key).decode('UTF-8')

    def get_int(self, key: str) -> int:
        """
            Automatically parametrize Cache.get
            with the correct conversion function.
        """
        try:
            return int(self._redis.get(key))
        except Exception:
            return 0
