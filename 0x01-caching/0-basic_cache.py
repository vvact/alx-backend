#!/usr/bin/env python3
"""
BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache module:
    Inherits from the BaseCaching module
    """
    def __init__(self):
        """Initializr class BasicCache"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        add an item to the caching system
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns: item associated with the key
        None if the key is not in the cache
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
