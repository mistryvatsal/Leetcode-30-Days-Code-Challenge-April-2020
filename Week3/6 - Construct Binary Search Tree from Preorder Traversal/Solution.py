#
# Created on Tue Apr 21 2020
#
# Title: Leetcode - Construct Binary Search Tree from Preorder Traversal
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        if len(preorder) == 0:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        smaller = list()
        greater = list()
        for i in range(1, len(preorder)):
            if preorder[i] < root_val:
                smaller.append(preorder[i])
            else:
                greater.append(preorder[i])
        root.left = self.bstFromPreorder(smaller)
        root.right = self.bstFromPreorder(greater)

        return root
