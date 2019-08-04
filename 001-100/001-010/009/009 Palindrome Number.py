###########################################################
# 009 Palindrome Number
#
# Description:
# Determine whether an integer is a palindrome. An integer
#  is a palindrome when it reads the same backward as forward.
#
# Example:
# Example 1:
# Input: 121
# Output: true
# 
# Example 2:
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# 
# Example 3:
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# Follow up:
# Coud you solve it without converting the integer to a string?
#
# Solution:
# 
###########################################################
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        integer = 0
        num = x
        if num<0:
            return False

        while num > 9:
            integer = integer*10 + num%10
            num = int(num/10)
        integer = integer * 10 + num
        if integer == x:
            return True
        else:
            return False
