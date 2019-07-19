## 题目
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
## 用例
### Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
## 方法一
### 想法
申请一个长度为数组中最大值的数组S，初始化为-1
如果 S[target-i] == -1 则与之对应的数为找到，
将S[i] 置为 该变量的位置
如果 S[target-i] != -1 则存在，返回 [S[i],S[target-i]]
```
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        enmuq={}
        enums=enumerate(nums) #枚举化
        for i, each in enums:
            if target-each in enmuq:
                return [enmuq[target-each], i]
            enmuq[each] = i
        return []
```
