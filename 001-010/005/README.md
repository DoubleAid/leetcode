## 题目
### 005 Longest Palindromic Substring
Given a string s, find the longest palindromic substring
in s. You may assume that the maximum length of s is 1000.

## 用例
### Example 1:
Input: "babad"  
Output: "bab"  
Note: "aba" is also a valid answer.  

### Example 2:
Input: "cbbd"  
Output: "bb"  

## 方法一
### 想法：
a#b#c#d
想象在每个元素间添加 # 那么如果只需要对称的查看中间点的左右
```
class Solution:
    def getLPDouble(self,s,i,j):
        count = 0
        while s[i] == s[j]:
            count += 2
            i -= 1
            j += 1
            if i<0 or j>=len(s):
                return count,s[i+1:j]
        return count,s[i+1:j]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        longestlen = 1
        longeststr = s[0]
        for i in range(1,2*len(s)-2):
            if i%2 == 1:
                i = i//2
                templen,tempstr = self.getLPDouble(s,i,i+1)
            else:
                i = i//2
                templen,tempstr = self.getLPDouble(s,i-1,i+1)
                templen += 1
            if templen >=longestlen:
                longestlen = templen
                longeststr = tempstr
        return longeststr
```
