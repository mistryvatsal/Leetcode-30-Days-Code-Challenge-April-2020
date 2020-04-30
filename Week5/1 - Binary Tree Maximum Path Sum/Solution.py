#
# Created on Thu Apr 30 2020
#
# Title: Leetcode - Binary Tree Maximum Path Sum
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

from sys import maxsize

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root):
        if root is None:
            return 0
        left_sum, right_sum = self.dfs(root.left), self.dfs(root.right)
        self.max_path_sum = max(self.max_path_sum, root.val + left_sum + right_sum)
        return max(0, root.val+max(left_sum, right_sum))

    def maxPathSum(self, root):
        self.max_path_sum = -maxsize
        self.dfs(root)
        return self.max_path_sum
