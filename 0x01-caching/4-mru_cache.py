#!/usr/bin/env python3
"""
This module contains clas MRUCache that inherits from BaseCache
and is a caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class inheriting from BaseCache class
    """
    def __init__(self):
        """class constructor"""
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """
        add iem into a cache
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.cache_data_list:
                self.cache_data_list.append(key)
            else:
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removed = self.cache_data_list.pop(-2)
                del self.cache_data[removed]
                print("DISCARD: {}".format(removed))

    def get(self, key):
        """
        retrieve an item fro cache
        """
        if key:
            if key in self.cache_data:
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
                return self.cache_data[key]
        return None
