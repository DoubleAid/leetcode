## 题目
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
## 用例
### Example 1:
```
Input: "1 + 1"
Output: 2
```
### Example 2:
```
Input: " 2-1 + 2 "
Output: 3
```
### Example 3:
```
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
```
#### Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
## 方法一
### 思路
刚开始觉得是一个简单的表达式
```
class Solution:
    def calculate(self, s: str) -> int:
        numstr = ""
        numstack = []
        charstack = []
        for each in s:
            if each == " ":
                continue
            if not each.isdecimal() and numstr != "":
                val2 = int(numstr)
                while charstack and charstack[-1] in ["+","-"]:
                    char = charstack.pop()
                    val1 = numstack.pop()
                    if char == "+":
                        val2 = val1 + val2
                    else:
                        val2 = val1 - val2
                numstr = ""
                numstack.append(val2)
            if each == "(":
                charstack.append(each)
            elif each == ")":
                charstack.pop()
                while charstack and charstack[-1] in ["+","-"]:
                    char = charstack.pop()
                    val2 = numstack.pop()
                    val1 = numstack.pop()
                    if char == "+":
                        val2 += val1
                    else:
                        val2 = val1 - val2
                numstack.append(val2)
            elif each in ["+","-"]:
                charstack.append(each)
            else:
                numstr += each
        if numstr != "":
            val2 = int(numstr)
        else:
            val2 = numstack.pop()
        while charstack:
            char = charstack.pop()
            val1 = numstack.pop()
            if char == "+":
                val2 += val1
            else:
                val2 = val1 - val2
        return val2
```
