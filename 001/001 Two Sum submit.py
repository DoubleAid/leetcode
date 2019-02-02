###########################################################
#001 Two Sum submit
#
#Introduce:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
#Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#Solution:
# ����һ������Ϊ���������ֵ������S����ʼ��Ϊ-1
# ��� S[target-i] == -1 ����֮��Ӧ����Ϊ�ҵ���
# ��S[i] ��Ϊ �ñ�����λ��
# ��� S[target-i] != -1 ����ڣ����� [S[i],S[target-i]]
###########################################################

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        enmuq={}
        enums=enumerate(nums) #ö�ٻ�
        for i, each in enums:
            if target-each in enmuq:
                return [enmuq[target-each], i]
            enmuq[each] = i
        return []


# if __name__ == "__main__":
#     app = Solution()
#     nums = [1,2,5,7,9,2,6,5,8,9,14,12,15]
#     print(app.twoSum(nums,15))