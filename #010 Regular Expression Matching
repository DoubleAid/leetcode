"""
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
"""





# class Solution:
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         slen = len(s)
#         plen = len(p)
#         arr = [([0] * slen) for i in range(plen)]
#         newp = p.replace('*','')
#         newplen = len(newp)
#         if newplen <= 0:
#             return False
#         for j in range(slen-newplen, -1,-1):
#             if p[0] == '.' or p[0] == s[j] or ( plen>=2 and p[1] == '*'):
#                 starti = 0
#                 while starti < plen and s[j] != p[starti] and p[starti] != ".":
#                     starti = starti + 1
#                 if starti < plen:
#                     arr[starti][j] = 1
#                 k = j + 1
#                 i = starti+1
#                 Maxcount = 1
#                 while i < plen:
#                     if k >= slen:
#                         break
#                     if p[i] == '*':
#                         for xk in range(k,slen):
#                             arr[i][xk] = arr[i-1][xk]
#                         if p[i-1] == '.':
#                             return True
#                         else:
#                             while k < slen and s[k] == p[i-1]:
#                                 arr[i][k] = arr[i-1][k-1] + 1
#                                 Maxcount = Maxcount + 1
#                                 k = k + 1
#                     elif p[i] == s[k] or p[i] == '.':
#                         arr[i][k] = arr[i - 1][k - 1] + 1
#                         Maxcount = Maxcount + 1
#                         k = k + 1
#                     else:
#                         break
#                     i = i + 1
#
#                 if Maxcount == slen:
#                     # for j in range(slen):
#                     #     print("  " + s[j], end="")
#                     # print("")
#                     # for i in range(plen):
#                     #     print(p[i] + str(arr[i]))
#                     # print("True")
#                     return True
#         # for j in range(slen):
#         #     print("  " + s[j], end="")
#         # print("")
#         # for i in range(plen):
#         #     print(p[i] + str(arr[i]))
#         # print("False")
#         return False


class Solution:
    def isMatch(self, s, p):
        newp = []
        if p == "":
            if s == "":
                return True
            return False
        i = 0
        while i < len(p) - 1:
            if p[i + 1] == '*':
                single = p[i] + p[i + 1]
                if len(newp) == 0 or (len(newp)>0 and newp[-1] != single):
                    newp.append(single)
                i = i + 1
            else:
                newp.append(p[i])
            i = i + 1
        if p[-1] != '*':
            newp.append(p[-1])
        return self.compare(s,newp)

    def compare(self,s,p):
        # print("s:"+str(s) +"  p:"+str(p))
        pstr = ""
        for each in p:
            pstr = pstr + each
        if s == pstr or (len(s) == 0 and len(p) - pstr.count("*") == 0):
            return True
        if len(s) < len(p) - pstr.count("*") or (len(p) == 0):
            return False
        if s[0] == p[0] or p[0] == '.':
            return self.compare(s[1:],p[1:])
        if p[0] == '.*':
            return self.compare(s[1:], p) or self.compare(s[1:], p[1:]) or self.compare(s,p[1:])
        if len(p[0]) == 2:
            resu = False
            if p[0][0] == s[0]:
                resu = self.compare(s[1:],p)
            return self.compare(s,p[1:]) or resu
        else:
            return False


if __name__ == "__main__":
    # s = "aa"
    # p = "a*"

    # s = 'aab'
    # p = 'c*a*b'

    # s = 'mississippi'
    # p = 'mis*is*p*.'

    # s = "aa"
    # p = "a"

    # s = "abcd"
    # p = "d*"

    # s = 'a'
    # p = 'b'

    # s = 'ab'
    # p = '.*'

    # s = 'ab'
    # p = '.*c'

    # s = 'a'
    # p = ''

    # s = "mississippi"
    # p = "mis*is*ip*."

    # s = "ab"
    # p = ".*.."

    s = "aaaaaaaaaaaaab"
    p = "a*a*a*a*a*a*b"

    print("s:" + str(s)+"  p:"+str(p))
    t = Solution()
    print(t.isMatch(s,p))
