#!/usr/bin/env python3
"""module with a cache class"""

import redis
import uuid
from typing import Union


class Cache:
    """a cache redis class"""
    def __init__(self):
        """store an instance then flush"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes data argument and returns a string.
        method generates a random key store the input data in Redis using
        the random key and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
