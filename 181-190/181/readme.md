# 题目
Given an array, rotate the array to the right by k steps, where k is non-negative.

# 例子
## Example 1:
Input: [1,2,3,4,5,6,7] and k = 3  
Output: [5,6,7,1,2,3,4]  
Explanation:  
rotate 1 steps to the right: [7,1,2,3,4,5,6]  
rotate 2 steps to the right: [6,7,1,2,3,4,5]  
rotate 3 steps to the right: [5,6,7,1,2,3,4]  

## Example 2:
Input: [-1,-100,3,99] and k = 2  
Output: [3,99,-1,-100]  
Explanation:   
rotate 1 steps to the right: [99,-1,-100,3]  
rotate 2 steps to the right: [3,99,-1,-100]  

## Note:

+ Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
+ Could you do it in-place with O(1) extra space?


## 方法一
### 想法:
求数组的长度numslen
求k的位置，将前 numslen-k 个元素从前面弹出，再从后面插入
```
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        numslen = len(nums)
        k = k % numslen
        for i in range(numslen-k):
            nums.append(nums.pop(0))
```
