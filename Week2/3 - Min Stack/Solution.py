#
# Created on Fri Apr 10 2020
#
# Title: Leetcode - Min Stack
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

class MinStack:
    def __init__(self):
        # Creating 2 stacks, stack : original data; currMinimum : to hold current minimum upon each push
        self.stack = list()
        self.currMinimum = list()

    def push(self, x: int) -> None:
        if len(self.stack) == 0 and len(self.currMinimum) == 0:
            self.stack.append(x)
            self.currMinimum.append(x)
        else:
            self.currMinimum.append(min(x, self.currMinimum[len(self.currMinimum) - 1]))
            self.stack.append(x)
            

    def pop(self) -> None:
        if not len(self.stack) == 0:
            self.stack.pop()
            self.currMinimum.pop()

    def top(self) -> int:
        if not len(self.stack) == 0:
            return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        if not len(self.currMinimum) == 0:
            return self.currMinimum[len(self.currMinimum) - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()