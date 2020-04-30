#
# Created on Thu Apr 30 2020
#
# Title: Leetcode - Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def is_valid(self, root, arr, index):
        if root.val != arr[index]:
            return False
        if index == len(arr) - 1:
            return not(root.left) and not(root.right)
        return ((root.left and self.is_valid(root.left, arr, index+1)) or (root.right and self.is_valid(root.right, arr, index+1)))
               

    def isValidSequence(self, root, arr):
        if root is None or len(arr) == 0:
            return False
        return self.is_valid(root, arr, 0)