#
# Created on Mon Apr 27 2020
#
# Title: Leetcode - Maximal Square
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

# Time Complexity = O(m * n)
# Space Complexity = O(m * n)
# Approach is to achieve iterative dynamic programming
class Solution:
    def maximalSquare(self, matrix):
        rows = len(matrix)
        # If empty matrix, then 0
        if rows == 0: return 0
        cols = len(matrix[0])
        # If row matrix is given then the maximalSquare area 
        # will be 1 if atleast one 1 present
        if rows == 1:
            if '1' in matrix[0]:
                return 1
            return 0
        # If column matrix is given then the maximalSquare area 
        # will be 1 if atleast one 1 prese
        if cols == 1:
            if any('1' in x for x in matrix[0]):
                return 1
            return 0
        # cache is same 2d matrix of size same as input matrix
        # approach will be to compute length of side of matrix
        # at the botton right of imaginary square 
        cache = [[0] * cols for _ in range(rows)]
        # we'll store latest max value in maximal
        maximal = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if (i==0) or (j==0):
                    cache[i][j] = int(matrix[i][j])
                if matrix[i][j] == '1':
                    cache[i][j] = 1 + min(int(cache[i-1][j-1]), int(cache[i-1][j]), int(cache[i][j-1]))
                    maximal = max(maximal, cache[i][j])
        # return the area of sqaure, where maximal is length of side
        return maximal ** 2

# Sample Input Case
obj = Solution()
matrix = [["1"]]
print(obj.maximalSquare(matrix))