#
# Created on Fri Apr 10 2020
#
# Title: Leetcode - Group Anagrams
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for i in strs:
            t = "".join(sorted(i))
            d.setdefault(t, []).append(i)
        o = list()
        for k, v in d.items():
            o.append(v)
        return o