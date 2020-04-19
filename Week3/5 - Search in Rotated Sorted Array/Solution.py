#
# Created on Sun Apr 19 2020
#
# Title: Leetcode - Search in Rotated Sorted Array
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

class Solution:
    def binarySearch(self, nums, low, high, target):
        if high >= low:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                return self.binarySearch(nums, low, mid-1, target)
            
            return self.binarySearch(nums, mid+1, high, target)
        return -1

    def findPivot(self, nums):
        return nums.index(min(nums))

    def search(self, nums, target):
        if(len(nums) == 0): return -1
        pivot = self.findPivot(nums)
        low = 0
        high = len(nums)-1
        if pivot == 0:
            return self.binarySearch(nums, low, high, target)

        if target == nums[pivot]:
            return pivot
        
        if nums[0] <= target:
            return self.binarySearch(nums, low, pivot-1, target)
        
        return self.binarySearch(nums, pivot+1, high, target)

# Sample Input
obj = Solution()
print(obj.search([4, 6, 7, 8, 1, 3], 7))