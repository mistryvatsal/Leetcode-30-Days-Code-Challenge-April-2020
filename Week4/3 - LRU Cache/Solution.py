#
# Created on Fri Apr 24 2020
#
# Title: Leetcode - LRU Cache
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

# Using OrderedDict, because it maintains the order of keys inserted as LIFO.
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        # Initialize cache size.
        self.cache_capacity = capacity
        # Create a hashmap/hashtable datastrcuture lookalike using OrderedDict
        self.hashmap = OrderedDict()

    def get(self, key):
        # Check if key is present in hashmap, if not return -1.
        if key in self.hashmap:
            # If key is present, pop the value for a while and push it again inorder to 
            # reorder the keys, and make this one as top, most recently used.
            value = self.hashmap.pop(key)
            self.hashmap[key] = value
            return value
        return -1

    def put(self, key, value):
        # If key is present in hashmap and pop it.
        if key in self.hashmap:
            self.hashmap.pop(key)
        # Demonstrating size of cache is full by checking length of hashmap with cache_capacity
        elif len(self.hashmap) == self.cache_capacity:
            # Pop the least recently used item. Do it by passing last=False
            # last=False makes the OrderedDict to popitem based on FIFO rather than LIFO
            # default value of argument last is True making the OrderedDict LIFO
            self.hashmap.popitem(last=False)
        # Push the latest value
        self.hashmap[key] = value
        