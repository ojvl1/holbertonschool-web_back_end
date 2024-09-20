#!/bin/python3
from base_caching import BaseCaching


"""FIFO caching"""


class FIFICache(BaseCaching):
    """Defining functions"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item
