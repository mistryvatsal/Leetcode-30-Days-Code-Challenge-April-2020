#
# Created on Fri Apr 10 2020
#
# Title: Leetcode - Happy Number
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

class Solution:
    def isHappy(self, n):
        seen = dict()
        while n is not 1:
            summ, curr = 0, n
            while curr is not 0:
                summ += (summ % 10) ** 2
                curr /= 10
            if(seen.__contains__(sum)):
                return False
            seen[summ] = summ
            n = summ
        return True
        