#
# Created on Sun Apr 12 2020
#
# Title: Leetcode - Last Stone Weight
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

class Solution:
    def lastStoneWeight(self, stones):
        if len(stones) == 0:
            return 0
        
        elif len(stones) == 1:
            return stones[0]
        else:   
            stones.sort()
            while len(stones) > 1:
                x, y = stones[-2], stones[-1]
                if x < y:
                    stones.pop()
                    stones.pop()
                    stones.append(y - x)
                    stones.sort()
                else:
                    stones.pop()
                    stones.pop()
            
            if len(stones):
                return stones.pop()
            else:
                return 0