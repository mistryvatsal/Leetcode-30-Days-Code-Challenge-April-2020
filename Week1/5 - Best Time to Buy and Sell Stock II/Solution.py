#
# Created on Fri Apr 10 2020
#
# Title: Leetcode - Best TIme to Buy and Sell Stock II
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        for i in range(len(prices) - 1):
            answer += max(0, prices[i + 1] - prices[i])
        return answer