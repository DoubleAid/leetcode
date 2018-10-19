"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nlist=[]
        mlist=[]
        mlist.extend(nums)
        mlist.sort()
        Tlist=self.mymergecompare(mlist,target)
        for i in Tlist:
            print(i)
            nlist.append(nums.index(i))
        return nlist

    def mymergecompare(self,nums,target):
        """
        :param nums:
        :param target:
        :return:
        """

        Mlist = []
        if len(nums) <= 1 :
            return list
        if nums[-1]+nums[0] >target:
            Mlist = self.mymergecompare(nums[0:-1],target)
        elif nums[-1]+nums[0] < target:
            Mlist = self.mymergecompare(nums[1:],target)
        else:
            Mlist.append(nums[0])
            Mlist.append(nums[-1])
        return Mlist

    """
    problem:Memory Limit Exceeded 
    """
