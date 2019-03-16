###########################################################
# 006 ZigZag Conversion
# 
# Description:
# The string "PAYPALISHIRING" is written in a zigzag pattern
#  on a given number of rows like this: (you may want to
#  display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);
# 
# Example:
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
# Solution: 
#  1     7
#  2   6 8
#  3 5   9
#  4     10
# 先找出第一行的数字 即 1 和 7
# 然后在从 1 到 numRows-1 的 i
# 加上 1,7,...左右两侧的 i 数
# 最后再加上最后一行
###########################################################
class Solution:
    def convert(self, s, numRows):
        strn = ""
        tk = []
        count=0
        strnlen = len(s)
        if strnlen<= numRows or numRows==1:
            return s
        while count<strnlen:
            tk.append(count)
            strn = strn + s[count]
            count = count + (numRows-1)*2
        tk.append(count)
        for i in range(1,numRows-1):
            for each in tk:
                if each-i>0 and each-i<strnlen :
                    strn = strn + s[each-i]
                if each+i<strnlen:
                    strn = strn + s[each+i]
        for each in tk:
            if each+numRows-1 < strnlen:
                strn = strn + s[each+numRows-1]
        return strn
