#!/usr/bin/env python3
"""1. Cache class with init and store method"""
import redis
import uuid
from typing import Union


class Cache:
    """Cache class to implement redis"""

    def __init__(self):
        """Create and store an instance of Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data:Union[str, bytes, int, float]) -> str:
        """Generate a random key and return it"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
