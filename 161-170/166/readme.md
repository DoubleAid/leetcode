## 题目

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.
## 用例
### Example 1:
```
Input: numerator = 1, denominator = 2
Output: "0.5"
```
### Example 2:
```
Input: numerator = 2, denominator = 1
Output: "2"
```
### Example 3:
```
Input: numerator = 2, denominator = 3
Output: "0.(6)"
```
## 方法一
### 思路
整数部分不用管，小数部分做字典标记，当发现有循环时，直接定位到相应的位置
#### time 100% memory 9.59%
```
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        flag = ""
        if numerator*denominator < 0:
            flag = "-"
            numerator = -numerator
        result = flag+str(numerator//denominator)+"."
        numer = (numerator % denominator)*10
        recu = {}
        count = 0
        presult = ""
        while numer not in recu:
            recu[numer] = count
            count += 1
            presult += str(numer//denominator)
            numer = (numer % denominator)*10
        starter = recu[numer]
        if numer == 0:
            if presult == "0":
                return result[:-1]
            return result+presult[:-1]
        return result + presult[:starter]+"("+presult[starter:]+")"
```
