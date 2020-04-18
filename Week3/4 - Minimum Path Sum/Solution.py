#
# Created on Sat Apr 18 2020
#
# Title: Leetcode - Minimum Path Sum
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

class Solution:
    def minPathSum(self, grid):
        if len(grid) == 0:
            return 0
        
        M = len(grid)
        N = len(grid[0])
        
        dp = [[int(0)]*N]*M
        dp[0][0] = grid[0][0]
        
        for i in range(M):
            for j in range(N):
                if i==0 and j==0:
                    dp[i][j] = grid[i][j]
                elif i==0 and j>0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif i>0 and j==0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[M-1][N-1]

# Sample input case
obj = Solution()
inpList = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

print(obj.minPathSum(inpList))