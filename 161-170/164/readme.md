## 题目
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

## 用例
### Example 1:
```
Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
```
### Example 2:
```
Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
```
### Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.

## 方法一
### 思路
因为是在一个范围内随机分布，可以使用桶排序的类似方法，
首先确认桶长:(maxv - minv)//(len-1)
每个桶维护一个最大值和一个最小值
```
class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        max_value = max(nums)
        min_value = min(nums)
        bin_len = (max_value - min_value)//(len(nums)-1)
        bin_len = max(bin_len,1)
        records = {}
        for val in nums:
            k = val // bin_len
            if k in records:
                records[k][0] = min(records[k][0],val)
                records[k][1] = max(records[k][1],val)
            else:
                records[k] = [val,val]
        pre = min_value
        result = 0
        for i in range(min_value//bin_len,(max_value//bin_len)+1):
            if i in records:
                result = max(records[i][0]-pre,result)
                pre = records[i][1]
        return result
```
