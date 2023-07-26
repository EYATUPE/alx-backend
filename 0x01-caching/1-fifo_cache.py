#!/usr/bin/python3
""" a class FIFOCache that inherits from BaseCaching and is a caching system """

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Represents an object that allows storing and
    retrieving of items from a dictionary with a FIFO
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """ Initializes the cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ adds an item in the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
