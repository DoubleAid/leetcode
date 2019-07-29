## 题目
Reverse bits of a given 32 bits unsigned integer.
## 用例
### Example 1:
```
Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
```
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
### Example 2:
```
Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
```
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10101111110010110010011101101001.
 
#### Note:
Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 
#### Follow up:
If this function is called many times, how would you optimize it?
## 方法一
### 思路
32次循环，每次提取一位比特数，放到结果中去，再乘以二
#### time 99.26% memory 37.77%
```
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            val = n % 2
            n = n // 2
            result = result*2 + val
        return result
```
