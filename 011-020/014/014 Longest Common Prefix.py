###########################################################
# 014 Longest Common Prefix
#
# Description:
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# 
# Example:
# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# Note:
# All given inputs are in lowercase letters a-z.
# 
# Solution:
#   ������Ӵ�����
#   ���ǰ׺����ֻҪ����ǰ�濪ʼ�ȽϾͺ���
#   ����Ҫ�������⣬����Ҫ��ʲô
#   ǰ�����Ƚϵó�ǰ׺��֮��һ�κ���һ���ַ������Ƚ�
###########################################################
class Solution:
    def LongestPrefix(self,str1,str2):
        row = len(str1)
        collow = len(str2)
        if row == 0 or collow == 0:
            return ""
        i = 0
        for i in range(min(row,collow)):
            if str1[i] != str2[i]:
                return str1[0:i]
        return str1[0:i+1]

    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        comp = self.LongestPrefix(strs[0],strs[1])
        if len(strs)==2:
            return comp
        for each in range(2,len(strs)):
            comp = self.LongestPrefix(comp,strs[each])
        return comp

if __name__ == "__main__":
    app = Solution()
    # strs=["flower","flow","flight"]
    # strs=["dog","racecar","car"]
    # strs  = ["ca","a"]
    # strs = ["a","ac"]
    strs = ["baab","bacb","b","cbc"]
    print(app.longestCommonPrefix(strs))

        