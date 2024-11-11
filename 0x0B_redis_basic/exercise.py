#!/usr/bin/env python3
"""Writing strings to Redis"""


import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    ''' def count calls '''
    @wraps(method)
    def wrapper(self, *args, **kwds):
        ''' def wrapper '''
        key_m = method.__qualname__
        self._redis.incr(key_m)
        return method(self, *args, **kwds)
    return wrapper

def call_history(method: Callable) -> Callable:
    ''' def call history '''
    @wraps(method)
    def wrapper(self, *args, **kwds):
        ''' def wrapper'''
        key_m = method.__qualname__
        inp_m = key_m + ':inputs'
        outp_m = key_m + ":outputs"
        data = str(args)
        self._redis.rpush(inp_m, data)
        fin = method(self, *args, **kwds)
        self._redis.rpush(outp_m, str(fin))
        return fin
    return wrapper

class Cache():
    def __init__(self):
        """
        Initialize the Cache instance
        with a Redis client and flush the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis with a randomly generated key
        Args:
            data: The data to store (can be str, bytes, int, or float)
        Returns:
        A string representing the generated key
        """
        mykey = str(uuid.uuid4())  # Generate a random key
        self._redis.set(mykey, data)
        return mykey

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, int, bytes, None]:
        value = self._redis.get(key)
        
        if value is None:
            return None
        
        if fn:
            return fn(value)
        
        return value

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, fn=int)
