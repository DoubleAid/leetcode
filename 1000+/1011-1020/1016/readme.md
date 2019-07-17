
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1,N+1):
            temp = ""
            while i:
                temp = str(i%2)+temp
                i >>= 1
            if temp not in S:
                return False
        return True
