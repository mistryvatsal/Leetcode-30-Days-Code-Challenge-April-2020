#
# Created on Sun Apr 12 2020
#
# Title: Leetcode - Diameter of Binary Tree
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.answer = 1
        
        def depth(node):
            if not node:
                return 0    
            L = depth(node.left)
            R = depth(node.right)

            self.answer = max(self.answer, 1 + R + L)
            return max(L, R) + 1
        
        depth(root)
        return self.answer - 1