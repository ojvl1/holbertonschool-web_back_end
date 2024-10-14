#!/usr/bin/python3
"""FIFO caching"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Defining functions
        - put function: implementing FIFO algorithm
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            self.cache_data[key] = item

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_item = next(iter(self.cache_data))
            print(f"DISCARD: {first_item}")
            self.cache_data.pop(first_item)

    def get(self, key):
        valuecache = self.cache_data.get(key)
        return valuecache
