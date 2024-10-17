#!/usr/bin/env python3
"""
This module contains class LIFOCache that inherits from
BaseCache and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class inheriting from BaseCache class"""
    def __init__(self):
        """
        class constructor
        """
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """
        add item into a cache
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key_2nd_last = len(self.cache_data_list) - 2
                key_last = self.cache_data_list.pop(key_2nd_last)
                del self.cache_data[key_last]
                print("DISCARD: {}".format(key_last))

    def get(self, key):
        """
        retrieve an item from cache
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
