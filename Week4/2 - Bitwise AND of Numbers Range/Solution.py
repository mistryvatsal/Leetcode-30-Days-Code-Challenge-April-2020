#
# Created on Thu Apr 23 2020
#
# Title: Leetcode - Bitwise AND of Numbers Range
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

class Solution:
    def bitwiseAnd(self, m, n):
        count = 0
        while m < n:
            m >> 1
            n >> 1
            count += 1
        return m << count