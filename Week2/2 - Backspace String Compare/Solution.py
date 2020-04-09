#
# Created on Fri Apr 10 2020
#
# Title: Leetcode - Backspace String Compare
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

class Solution:
    def stringify(self, string):
        stringList = list()
        for i in string:
            if i != "#":
                stringList.append(i)
            elif len(stringList) != 0:
                stringList.pop()
        return "".join(stringList)
    
    def backspaceCompare(self, S, T):
        return self.stringify(S) == self.stringify(T)