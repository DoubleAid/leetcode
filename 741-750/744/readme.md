# 题目
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

# 用例

## Examples:
Input:  
letters = ["c", "f", "j"]  
target = "a"  
Output: "c"  

Input:  
letters = ["c", "f", "j"]  
target = "c"  
Output: "f"  

Input:  
letters = ["c", "f", "j"]  
target = "d"  
Output: "f"  

Input:
letters = ["c", "f", "j"]  
target = "g"  
Output: "j"  

Input:
letters = ["c", "f", "j"]  
target = "j"  
Output: "c"  

Input:
letters = ["c", "f", "j"]  
target = "k"  
Output: "c"  
## Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
## 方法一
### 想法
注意 ascill码和字符的相互转换 ord()和chr()的用法
做一个26个字母的标记位，如果存在，标记位大于零，这样只要利用余数循环查询一遍就能找到了
```
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        tips = [ 0 for i in range(26)]
        for each in letters:
            tips[ord(each)-97] += 1
        start = ord(target) - 96
        while True:
            key = start % 26
            if tips[key] > 0:
                return chr(97 + key)
            start += 1

```
