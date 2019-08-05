## 题目
etermine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
## 用例
### Example 1:

Input: s = "egg", t = "add"
Output: true
### Example 2:

Input: s = "foo", t = "bar"
Output: false
### Example 3:

Input: s = "paper", t = "title"
Output: true
### Note:
You may assume both s and t have the same length.
## 方法一
### 思路
在两个字符上做映射，不用两个都是映射，一个映射，一个字符串
```
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        yingshe = {}
        already = ""
        for i in range(len(s)):
            if s[i] not in yingshe:
                if t[i] in already:
                    return False
                yingshe[s[i]] = t[i]
                already += t[i]
            if t[i] != yingshe[s[i]]:
                return False
        return True
```
