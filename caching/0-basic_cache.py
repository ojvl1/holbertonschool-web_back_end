#!/usr/bin/python3
"""Basic dictionary"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):

    """Defining the functions
        - put function: assign the dictionary self.cache_data
        the item value for the key 'key'
        - get function: return the value in self.cache_data
        liinked to key
    """

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """return value of the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
