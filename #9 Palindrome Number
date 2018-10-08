class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        integer = 0
        num = x
        if num<0:
            return False

        while num > 9:
            integer = integer*10 + num%10
            num = int(num/10)
        integer = integer * 10 + num
        if integer == x:
            return True
        else:
            return False
