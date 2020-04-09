#
# Created on Fri Apr 10 2020
#
# Title: Leetcode - Middle of the Linked List
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p1 = p2 = head
        while p1 != None and p1.next != None:
            p1, p2 = p1.next.next, p2.next
        return p2