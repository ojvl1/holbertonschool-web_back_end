#!/usr/bin/env python3
"""Writing strings to Redis"""


import redis
import uuid
from typing import Union


class Cache():
    def __init__(self):
        """
        Initialize the Cache instance
        with a Redis client and flush the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

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
