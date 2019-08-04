###########################################################
# 017 Letter Combinations of a Phone Number
# 
# Description:
#   Given a string containing digits from 2-9 inclusive, return
#  all possible letter combinations that the number could represent.
#  A mapping of digit to letters (just like on the telephone buttons)
#  is given below. Note that 1 does not map to any letters.
#
#    1 ___    2 abc    3 def
#    4 ghi    5 jkl    6 mno
#    7 pqrs   8 tuv    9 wxyz
#             0 ___
#
# Example:
#   Input: "23"
#   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
# 
# Note:
#   Although the above answer is in lexicographical order,
#  your answer could be in any order you want. 
# 
# Solution:
#   
###########################################################
class Solution:
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        reference = { "1":"", "2":"abc", "3":"def",
                      "4":"ghi", "5":"jkl", "6":"mno",
                      "7":"pqrs","8":"tuv","9":"wxyz",
                      "0":""}
        listn = []
        for digit in digits:
            if reference[digit] != "":
                listn.append(reference[digit])
        if len(listn)<1:
            return []
        elif len(listn) == 1:
            return self.divide(listn[0])
        s = self.divide(listn[0])
        for li in listn[1:]:
            lin = self.divide(li)
            s = self.combine(s,lin)
        return s

    def combine(self,li1,li2):
        print(li1)
        print(li2)
        result = []
        for i in li1:
            for j in li2:
                result.append(str(i)+str(j))
        return result

    def divide(self,s):
        m = []
        for i in s:
            m.append(i)
        return m

if __name__ == "__main__":
    app = Solution()
    strn = "22"
    listn = app.letterCombinations(strn)
    print(listn)