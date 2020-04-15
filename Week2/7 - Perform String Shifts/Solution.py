#
# Created on Wed Apr 15 2020
#
# Title: Leetcode - Perform String Shifts
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]):
        totalAmount = 0
        for p in shift:
            if p[0] == 0:
                totalAmount -= p[1]
            else:
                totalAmount += p[1]

        n = len(s)
        totalAmount %= n
        if totalAmount < 0 :
            totalAmount += n
            
        return s[n - totalAmount:] + s[0: n - totalAmount]