#
# Created on Wed Apr 15 2020
#
# Title: Leetcode - Product of Array Except Self
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

# Time Complexity : O(n)
# Space Complexity : O(n)

class Solution:
    def productExceptSelf(self, nums):
        leftProduct = [None] * len(nums)
        rightProduct = [None] * len(nums)

        leftProduct[0] = rightProduct[-1] = 1

        for i in range(1, len(nums)):
            leftProduct[i] = leftProduct[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            rightProduct[i] = rightProduct[i + 1] * nums[i + 1]
        
        return [i*j for (i, j) in zip(leftProduct, rightProduct)]


