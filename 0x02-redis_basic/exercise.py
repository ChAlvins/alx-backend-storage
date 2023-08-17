#!/usr/bin/env python3
"""module with a cache class"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count how many times methods of the Cache class are called."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrap decorated function and return the wrapper"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """a cache redis class"""
    def __init__(self):
        """store an instance then flush"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes data argument and returns a string.
        method generates a random key store the input data in Redis using
        the random key and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn:
            Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """convert the data back to the desired format."""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is None:
            return data
        return fn(data)

    def get_str(self, key: str) -> Union[str, None]:
        """ parametrize Cache.get with correct conversion function"""
        data = self._redis.get(key)
        return data.decode('utf-8')

    def get_int(self, key: str) -> Union[int, None]:
        """parametrize Cache.get with the correct conversion function"""
        return self.get(key, fn=int)
