## 题目
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
## 用例
### Example 1:

Input: a = 1, b = 2
Output: 3
### Example 2:

Input: a = -2, b = 3
Output: 1
### 方法一
```
class Solution(object):
    def getSum(self, a, b):
        result = ( a ^ b ) & 0xffffffff
        carry = ((a & b) << 1) & 0xffffffff
        if carry != 0:
            result = self.getSum(result,carry)
        return result if result <= 0x7fffffff else ~(result ^ 0xffffffff)
```
