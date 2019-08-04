## 题目
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

### Note:
+++ The same word in the dictionary may be reused multiple times in the segmentation.
+++ You may assume the dictionary does not contain duplicate words.
## 用例
### Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
### Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
### Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
## 方法一
### 想法:  
动态规划
```
class Solution:
    def wordBreak(self, s: str, wordDict):
        lendict = {}
        for each in wordDict:
            wlen = len(each)
            if wlen not in lendict:
                lendict[wlen] = [each]
            else:
                lendict[wlen].append(each)
        sdp = [False for i in range(len(s)+1)]
        sdp[-1] = True
        for i in range(len(s)):
            for each in lendict:
                if sdp[i-each]:
                    if self.isSame(s[i-each+1:i+1],lendict[each]):
                        sdp[i] = True
        return sdp[-2]

    def isSame(self,str1,str2s):
        k = []
        try:
            for each in str2s:
                if str1[0] == each[0]:
                    k.append(each)
            for i in range(1,len(str1)):
                for j in range(len(k)):
                    ele = k.pop(0)
                    if str1[i] == ele[i]:
                        k.append(ele)
        except:
            return False
        if k:
            return True
        return False
```
