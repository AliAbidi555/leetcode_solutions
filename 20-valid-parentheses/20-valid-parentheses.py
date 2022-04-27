class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')','{':'}','[':']'}
        stack = []
        for i in s: 
            if i in ['(','[','{']:
                stack.append(i)
            else: 
                if stack and i == brackets[stack[-1]]:
                    stack.pop(-1)
                else:
                    return(False)
        if stack:
            return(False)
        else:
            return(True)
                