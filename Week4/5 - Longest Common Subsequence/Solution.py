#
# Created on Mon Apr 27 2020
#
# Title: Leetcode - Longest Common Subsequence
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

# Time complexity : O(m*n)
# Space complexity : O(m*n)

class Solution:
    # Dynamic programming implementation
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1) + 1, len(text2) + 1
        # Create a 2D array / matrix and initialize with zero
        table = m * [[0] * n]
        for i in range(1, m):
            for j in range(1, n):
                if text1[i-1] == text2[j-1]:
                    table[i][j] = 1 + table[i-1][j-1]
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])
        # The last element will hold the length of LCS, hence return that
        return table[m-1][n-1]

# Sample input case
obj = Solution()
print("Answer : {}".format(obj.longestCommonSubsequence("abcdef", "bce")))
        