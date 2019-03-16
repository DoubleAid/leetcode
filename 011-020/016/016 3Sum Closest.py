###########################################################
# 016 3Sum Closest
# 
# Description:
#   Given an array nums of n integers and an integer target, 
#   find three integers in nums such that the sum is closest to 
#   target. Return the sum of the three integers. You may assume
#   that each input would have exactly one solution.
#
# Example:
#   Given array nums = [-1, 2, 1, -4], and target = 1.
#   The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
# Solution:
###########################################################
class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        nums.sort()
        self.target = target
        self.result = nums[0]+nums[1]+nums[-1]
        self.absvalue = self.absn(target-self.result)
        i = 0
        while i < len(nums)-2:
            temp = nums[i]+nums[i+1]+nums[len(nums)-1]
            tempvalue = self.absn(target-temp)
            if tempvalue < self.absvalue:
                self.result = temp
                self.absvalue = tempvalue
            self.comp(nums,i,i+1,len(nums)-1,tempvalue)
            i += 1
            while i<len(nums)-2 and nums[i] == nums[i - 1]:
                i += 1
        return self.result

if __name__ == "__main__":
    app = Solution()
    # nums= [-1, 2, 1, -4] #1
    # nums = [0,2,1,-3]
    # nums = [1,1,-1,-1,3]
    # nums = [-1,0,1,1,55] #3
    nums = [-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33]  #0
    result = app.threeSumClosest(nums,0)
    print(result)    