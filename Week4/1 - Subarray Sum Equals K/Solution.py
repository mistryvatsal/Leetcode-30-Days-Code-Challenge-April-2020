#
# Created on Thu Apr 23 2020
#
# Title: Leetcode - Subarray Sum Equals K
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

class Solution:
    def subarraySum(self, nums, k):
        curr_sum = count = 0
        # Creating hash map with dictionary and assigning (0: 1) pair manually.
        # Space : O(N)
        hash_map = {0: 1}
        # Time : O(N)
        for i in nums:
            curr_sum += i
            if curr_sum - k in hash_map:
                count += hash_map[curr_sum - k]
            hash_map[curr_sum] = hash_map.get(curr_sum, 0) + 1
        return count

# Sample input case
obj = Solution()
print(obj.subarraySum([1, 2, 3], 3))