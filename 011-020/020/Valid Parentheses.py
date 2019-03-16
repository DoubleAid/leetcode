###########################################################
# 20. Valid Parentheses
# 
# Description:
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# Example:
# Example 1:
# Input: "()"
# Output: true
# 
# Example 2:
# Input: "()[]{}"
# Output: true
# 
# Example 3:
# Input: "(]"
# Output: false
# 
# Example 4:
# Input: "([)]"
# Output: false
# 
# Example 5:
# Input: "{[]}"
# Output: true
#
# Solution:
#
###########################################################

class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(','[','{']
        right = [')',']','}']
        stack = []
        for i in s:
            if i in left:
                stack.append(i)
            if i in right:
                if len(stack) == 0:
                    return False
                j = stack.pop()
                if left.index(j) == right.index(i):
                    continue
                else:
                    return False
        if len(stack) != 0:
            return False
        return True
