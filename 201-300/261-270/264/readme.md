## 题目
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
## 用例
### Example:
```
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
```
### Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
## 方法一
### 思路
排序找当前最小的丑数
```
class Solution(object):
    def nthUglyNumber(self, n):
        li = [1]
        th2,th3,th5 = 0,0,0 
        for i in range(1,n):
            val = min(li[th2]*2,li[th3]*3,li[th5]*5)
            li.append(val)
            if li[th2]*2 <= val:
                th2 += 1
            if li[th3]*3 <= val:
                th3 += 1
            if li[th5]*5 <= val:
                th5 += 1
        return li[-1]
```
