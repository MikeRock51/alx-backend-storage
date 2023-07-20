#!/usr/bin/env python3
"""Exploring Redis basics/ Redis-py"""

from redis import Redis
from uuid import uuid4
from typing import Union


class Cache:
    """Caching with Redis"""

    def __init__(self):
        """Stores a Redis instance"""
        self.__redis = Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in redis and returns the ID"""

        id: str = str(uuid4())
        self.__redis.set(id, data)

        return id
