class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        a=s.split(' ')        
        max = 0
        print(a)
        for i in a: 
            if i.isdigit():
                if int(i) <= max:
                    return(False)
                else:
                    max = int(i)
        return(True)