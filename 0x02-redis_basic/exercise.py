#!/usr/bin/env python3
"""0. Cache class with init and store method
1. Byte to str or int"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """Cache class to implement redis"""

    def __init__(self):
        """Create and store an instance of Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key and return it"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def get(key: str,
            fn: Optional[callable] = None) -> Union[str, bytes, int, float]:
        """Function to convert the stored byte data to readable format"""
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_int(self, key: str) -> int:
        """Decode the value returned from the get method"""
        data = self._redis.get(key)
        try:
            data = int(data.decode("utf-8")
        except Exception:
            data=0
        return data

    def get_str(self, key: str) -> str:
        """Decode data to int"""
        data=self._redis.get(key)
        return data.decode("utf-8")
