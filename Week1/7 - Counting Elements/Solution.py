#
# Created on Fri Apr 10 2020
#
# Title: Leetcode - Counting Elements
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

class Solution:
    def countElements(self, arr):
        d = dict((ele, arr.count(ele)) for ele in arr)
        count = 0
        for ele in arr:
            if (ele + 1) in d.keys():
                count += 1
        return count