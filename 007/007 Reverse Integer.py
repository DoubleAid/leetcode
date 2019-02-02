###########################################################
# 006 ZigZag Conversion
# 
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example:
# Example 1:
# Input: 123
# Output: 321
# 
# Example 2:
# Input: -123
# Output: -321
# 
# Example 3:
# Input: 120
# Output: 21
# 
# Solution:
# 首先去掉符号位
# 再取余数乘以十
# 最后再称上符号位
###########################################################
class Solution:
    def reverse(self, x):
        num = x
        isNegative = 1
        if num==0:
            return x
        if  num<-pow(2,31) or num>pow(2,31)-1:
            return 0
        if num<0:
            isNegative = -1
            num = -num
        while num%10 == 0:
            num=int(num/10)
        strn = str(num)
        strn = strn[::-1]
        interg = int(strn)*isNegative
        if interg<-pow(2,31) or interg>pow(2,31)-1:
            return 0
        return interg
