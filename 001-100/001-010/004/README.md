## 题目
### 004 Median of Two Sorted Array
There are two sorted arrays nums1 and nums2 of size m and n respectively.  
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).  
You may assume nums1 and nums2 cannot be both empty.
## 用例
### Example 1:
nums1 = [1, 3]  
nums2 = [2]  
The median is 2.0  

### Example 2:
nums1 = [1, 2]  
nums2 = [3, 4]  
The median is (2 + 3)/2 = 2.5
## 方法一
### 想法：
类似于归并算法，从开始检索最小值，排序排到中间值即可
```
class Solution:
    def findMedianSortedArrays(self,nums1,nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result = 0
        current = 0
        median = (len(nums1) + len(nums2))
        if median%2 == 1:
            median1= median//2
            median2 = median1
        else:
            median1 = median//2-1
            median2 = median1+1
        i,j = 0,0 
        while len(nums1) != i and len(nums2) != j:
            if nums1[i]>nums2[j]:
                value = nums2[j]
                j += 1
            else:
                value = nums1[i]
                i += 1
            current += 1
            if current-1 == median1:
                result = value
            if current-1 == median2:
                return (result+value)/2 
        listn = nums1 if len(nums1)!=i else nums2
        i = i if len(nums1) != i else j
        i += (median2 - current)
        if result == 0:
            if median1 == median2:
                result += listn[i]
            else:
                result += listn[i-1]
        return (result+listn[i])/2
```
