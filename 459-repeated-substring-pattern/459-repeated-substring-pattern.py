class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)
        for i in range(1,N):
            if N%i==0 and s[:i]*(N//i) == s:
                return(True)
            
        return(False)