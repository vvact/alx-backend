#!/usr/bin/env python3
"""
FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache module:
    Inherits from the BaseCaching module
    """
    def __init__(self):
        """
        Initialize class instance
        """
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """
        add an item to the caching system
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.cache_data_list[0])
                discard = self.cache_data_list.pop(0)
                print("DISCARD: {}".format(discard))

    def get(self, key):
        """
        Returns: item associated with the key
        None if the key is not in the cache
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
