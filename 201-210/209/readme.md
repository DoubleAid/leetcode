# 题目
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
# 用例
## Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
## Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
## 方法一
### 想法
使用两个指针start和end，指针内之和k
如果 k小于s，将end向右移动
如果 k大于s，将start向右移动，并且更新最短长度
### time 70%  memory 60%
```
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = nums[0]
        ans = 0
        start = 0
        end = 0
        while end < len(nums)-1:
            if result < s:
                end += 1
                result += nums[end]
            else:
                ans = min(ans,end-start+1) if ans > 0 else end-start+1
                result -= nums[start]
                start += 1
        if result < s:
            return ans
        while result >= s:
            result -= nums[start]
            start += 1
        return min(ans,end-start+2) if ans > 0 else end-start+2

```
