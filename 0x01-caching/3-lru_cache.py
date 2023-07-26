#!/usr/bin/env python3
"""A class Least Recently Used Cache that inherits from
BaseCaching and is a caching system:
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Represents an object that allows storing and
    retrieving items from a dictionary with a LRU
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """initialize the object's attributes
        """
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """to add or update an item in the cache
        based on the provided key

        Args:
                        key (_type_): _description_
                        item (_type_): _description_
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """returnss the value in self.cache_data linked to key

        Args:
                        key (_type_): _description_
        """
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None
