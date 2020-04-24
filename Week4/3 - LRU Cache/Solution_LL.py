#
# Created on Sat Apr 25 2020
#
# Title: Leetcode - LRU Cache
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

# A hashmap<int, Node> based approach where key is of type integer
# and value is of type Node which represents a node of a Doubly Linked List.

# Defining structure for Linked List node
class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity):
        # Cache capacity/size
        self.cache_capacity = capacity

        # Creating hashmap / hashtable using dictionary
        self.hashmap = dict()

        # Creating head and tail pointer and assinging them to each other indicating
        # linked list is empty
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    # Utility function to add node to doubly linked list
    def add_node(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head = node

    # Utility function to remove node from doubly linked list
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        result = -1
        node = self.hashmap.get(key)
        if node is not None:
            result = node.value
            self.remove_node(node)
            self.add_node(node)

        return result

    def put(self, key, value):
        node = self.hashmap.get(key)
        if node is not None:
            self.remove_node(node)
            node.value = value
            self.add_node(node)
        else:
            if len(self.hashmap) == self.cache_capacity:
                self.hashmap.pop(self.tail.value)
                self.remove_node(self.tail.prev)
            
            node = Node(value)
            self.add_node(node)
            self.hashmap[key] = node
