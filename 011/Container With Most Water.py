###########################################################
# 011 Container With Most Water 
# 
# Description:
#  Given n non-negative integers a1, a2, ..., an , where each
#   represents a point at coordinate (i, ai). n vertical lines
#   are drawn such that the two endpoints of line i is at (i, ai)
#   and (i, 0). Find two lines, which together with x-axis forms
#   a container, such that the container contains the most water.
#  Note: You may not slant the container and n is at least 2.
#
# Example:
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

# Solution:
#   我刚开始时觉得先找到最大的两个数，再向外扩散，但会出现有一点在
#   两个最大值中间的情况
#   其实原理一样，从最外层向内查找即可
###########################################################
class Solution:
    def calculate(self,height,left,right):
        return (right-left)*min(height[left],height[right])
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maxarea = self.calculate(height,left,right)
        while(left<right):
            if height[left]>height[right]:
                right -= 1
            else:
                left += 1
            maxarea = max(maxarea,self.calculate(height,left,right))
        return maxarea

if __name__ == "__main__":
    app = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(app.maxArea(height))
