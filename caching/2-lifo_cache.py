#!/usr/bin/python3
"""LIFO algorithm"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Defining functions"""
    def __init__(self):
        super().__init__()
        self.last_item = None

    def put(self, key, item):
        if key is None or item is None:
            self.cache_data[key] = item

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.last_item is not None:
                print(f"DISCARD: {self.last_item}")
                del self.cache_data[self.last_item]

        self.last_item = key

    def get(self, key):
        if key is None or key not in self.cache_data:
            return self.cache_data.get(key)
