###########################################################
#003 Longest Substring Without Repeating 
# 
# Introduce:
# Given a string, find the length of the longest substring without repeating characters.
# 
# Example:
# Example 1:
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
# Solution:
# ά��һ��������ı������¼���һ�μ����λ�ã���󳤶�Ϊ���һ�μ�������ǰ���������Ĳ�ֵ
###########################################################
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        length=-1
        startaddress=0
        i=0
        for i in range(1,len(s)):
            if s[i] in s[startaddress:i]:
                m=s[startaddress:i].find(s[i])
                length=max(length,i-startaddress)
                startaddress=startaddress+m+1
        length=max(length,i-startaddress+1)
        return length
if __name__ == "__main__":
    s = Solution()
    # strn='bziuwnklhqzrxnb'
    # strn='aab'
    # strn=' '
    # strn='abcabcbb'
    print(s.lengthOfLongestSubstring(strn))
