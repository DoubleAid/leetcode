class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        enmuq={}
        enums=enumerate(nums)
        for i, each in enums:
            if target-each in enmuq:
                return [enmuq[target-each], i]
            enmuq[each] = i
        return []
