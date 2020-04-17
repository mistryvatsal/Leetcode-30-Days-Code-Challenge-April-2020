#
# Created on Fri Apr 17 2020
#
# Title: Leetcode - Number of Islands
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

class Solution:
    def bfs(self, grid, i, j):
        
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0":
            return None
        
        grid[i][j] = "0"
        
        self.bfs(grid, i, j+1)
        self.bfs(grid, i, j-1)
        self.bfs(grid, i+1, j)
        self.bfs(grid, i-1, j)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == str(1):
                    count += 1
                    self.bfs(grid, i, j)
        
        return count