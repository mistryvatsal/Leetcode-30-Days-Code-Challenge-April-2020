#
# Created on Fri Apr 10 2020
#
# Title: Leetcode - Maximum SubArray
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#
import sys

class Solution:
    
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1], nums[0] + nums[1])
        else:
            mid = len(nums) // 2
            
            leftBest = -sys.maxsize - 1
            summ = 0
            for i in range(mid, -1, -1):
                summ += nums[i]
                leftBest = max(summ, leftBest)
            
            rightBest = -sys.maxsize - 1
            summ = 0
            for i in range(mid+1, len(nums)):
                summ += nums[i]
                rightBest = max(summ, rightBest)
            
            L = nums[0:mid+1]
            R = nums[mid+1:len(nums)]
            
            return max(self.maxSubArray(L), self.maxSubArray(R), leftBest+rightBest)