class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        num += s.count('I')-s.count('IV')-s.count('IX')
        num += 5*(s.count('V')-s.count('IV'))
        num += 10*(s.count('X') - s.count('IX') - s.count('XL') - s.count('XC'))
        num += 50*(s.count("L")-s.count("XL"))
        num += 100*(s.count("C")-s.count("XC")-s.count("CD")-s.count("CM"))
        num += 500*(s.count("D") - s.count("CD"))
        num += 1000*(s.count("M") - s.count("CM"))
        num += 4*(s.count('IV'))
        num += 9*(s.count('IX'))
        num += 40*(s.count('XL'))
        num += 90*(s.count('XC'))
        num += 400*(s.count('CD'))
        num += 900*(s.count('CM'))
        
        
        
        return(num)
            