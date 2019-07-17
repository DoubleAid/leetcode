# 题目
Given a binary string S (a string consisting only of '0' and '1's) and a positive integer N, return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.

# 用例
## Example 1:

Input: S = "0110", N = 3
Output: true
## Example 2:

Input: S = "0110", N = 4
Output: false
 

## Note:

1 <= S.length <= 1000
1 <= N <= 10^9

## 方法一
### 想法
将1到N的每一个数转化成二进制字符串，判断该字符串似不似S的子串
#### time 69% memory 17.89%
```
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1,N+1):
            temp = ""
            while i:
                temp = str(i%2)+temp
                i >>= 1
            if temp not in S:
                return False
        return True

```
