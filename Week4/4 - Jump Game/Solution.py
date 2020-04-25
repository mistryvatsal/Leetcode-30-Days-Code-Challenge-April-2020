#
# Created on Sat Apr 25 2020
#
# Title: Leetcode - Jump Game
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

# Approach will be to traverse array in reverse, maintain last_optimum_pos 
# and check whether last_optimum_pos is at the 0 index

class Solution:
    def canJump(self, nums):
        N = len(nums)
        last_optimum_pos = N-1
        for i in range(N-1, -1, -1):
            if (i + nums[i]) >= last_optimum_pos:
                last_optimum_pos = i
        
        return (last_optimum_pos == 0)