## 题目
Given a column title as appear in an Excel sheet, return its corresponding column number.
## 用例
For example:
```
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
```
### Example 1:
```
Input: "A"
Output: 1
```
### Example 2:
```
Input: "AB"
Output: 28
```
### Example 3:
```
Input: "ZY"
Output: 701
```
## 方法一
### 思路
做一个标记从后往前加上基值，之后基质每次乘以26
#### time 67.26% memory 50%
```
class Solution(object):
    def titleToNumber(self, s):
        slen = len(s)
        arr = [0 for i in range(slen)]
        tips = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7,
                "H":8, "I":9, "J":10,"K":11,"L":12,"M":13,"N":14,
                "O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,
                "V":22,"W":23,"X":24,"Y":25,"Z":26
               }
        result = 0
        base = 1
        while s != "":
            result += base*tips[s[-1]]
            s = s[:-1]
            base *= 26
        return result
```
