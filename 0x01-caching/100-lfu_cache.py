#!/usr/bin/env python3
""" a class Least Frequently Used Cache that inherits from BaseCaching and is a caching system
"""

from collections import defaultdict

class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.freq_counter = defaultdict(int)
        self.freq_map = defaultdict(list)

    def update_freq(self, key):
        freq = self.freq_counter[key]
        self.freq_counter[key] += 1
        self.freq_map[freq].remove(key)
        self.freq_map[freq + 1].append(key)

    def put(self, key, item):
        if key is None or item is None:
            return

        """ Check if key already exists, update frequency, and return """
        if key in self.cache_data:
            self.cache_data[key] = item
            self.update_freq(key)
            return

        """ If the cache is full, discard LFU items """
        if len(self.cache_data) >= self.MAX_ITEMS:
            min_freq = min(self.freq_map.keys())
            lfu_keys = self.freq_map[min_freq]

            """ If multiple LFU items exist, use LRU algorithm
            to discard the least recently used 
            """
            if len(lfu_keys) > 1:
                lru_key = self.queue.pop(0)
                while lru_key not in lfu_keys:
                    self.queue.append(lru_key)
                    lru_key = self.queue.pop(0)
                del self.cache_data[lru_key]
                self.freq_map[min_freq].remove(lru_key)
                print(f"DISCARD: {lru_key}")

            """ Remove the LFU key with the minimum frequency """
            lfu_key = lfu_keys[0]
            del self.cache_data[lfu_key]
            self.freq_map[min_freq].remove(lfu_key)
            print(f"DISCARD: {lfu_key}")

        """ Add the new item to the cache """
        self.cache_data[key] = item
        self.freq_counter[key] = 1
        self.freq_map[1].append(key)
        self.queue.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        self.update_freq(key)
        return self.cache_data[key]

cache = LFUCache()
cache.put(1, "Value1")
cache.put(2, "Value2")
cache.put(3, "Value3")
cache.get(1)
cache.put(4, "Value4")
cache.get(2)

