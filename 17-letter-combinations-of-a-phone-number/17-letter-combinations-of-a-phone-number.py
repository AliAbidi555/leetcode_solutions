import numpy 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if '' == digits: return []
        numpad = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        return reduce(lambda acc, digit: [x + y for x in acc for y in numpad[digit]], digits, [''])
        
                        