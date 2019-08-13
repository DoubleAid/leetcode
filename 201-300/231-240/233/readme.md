## 题目

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
## 用例
### Example:

Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

## 方法一
### 思路
按照位进行统计
分三类进行区别
第一种: 这个值为0，那么这个位1出现的次数为前缀*该位的位阶
```
class Solution:
    def countDigitOne(self, n: int) -> int:
        numstack = []
        value = n
        while value > 0:
            numstack.append(value%10)
            value = value//10
        total = 0
        front = 0
        nlen = len(numstack)
        while numstack:
            num = numstack.pop()
            nlen -= 1
            if num == 0:
                total += front*pow(10,nlen)
            elif num == 1:
                total += front*pow(10,nlen)+n%pow(10,nlen)+1
            else:
                total += (front+1)*pow(10,nlen)
            front = front*10+num
        return total
```
