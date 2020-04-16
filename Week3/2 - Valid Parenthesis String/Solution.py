#
# Created on Thu Apr 16 2020
#
# Title: Leetcode - Valid Parenthesis String
#
# Author: Vatsal Mistry
# Web: mistryvatsal.github.io
#

class Solution:
    def checkValidString(self, s):
        # Check if string is empty, if empty string then return True as empty string is given valid
        if s == "":
            return True
        
        # Create 2 list representing stacks.
        # main_stack for pushing index of left parenthesis.
        # star_stack for pushing index of star elements.
        main_stack = list()
        star_stack = list()

        # Iterate over string
        for index, val in enumerate(s):
            if val == '(':
                main_stack.append(index)
            elif val == '*':
                star_stack.append(index)
            
            # else case triggered whenever ')' is found. 
            else:

                # pop from main_stack if not empty
                if not len(main_stack) == 0:
                    main_stack.pop()
                
                # pop from star_stack if not empty. here * works like '(' 
                elif not len(star_stack) == 0:
                    star_stack.pop()
                
                # else case means no more * left to convert to '(', hence return False
                else:
                    return False
        
        # balancing the '(' in main_stack
        while not len(main_stack) == 0:
            if len(star_stack) == 0:
                return False
            elif main_stack[-1] < star_stack[-1]:
                main_stack.pop()
                star_stack.pop()
            else:
                return False
        
        return True

# Sample inputs.
obj = Solution()
print(obj.checkValidString("(*))"))
print(obj.checkValidString("(*)"))
print(obj.checkValidString("())"))