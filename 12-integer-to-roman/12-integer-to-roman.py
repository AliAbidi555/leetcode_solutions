class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        for _ in range(int(num/1000)):
            roman += 'M'    
        num = num % 1000    
        for _ in range(int(num/500)):
            roman += 'D'    
        num = num % 500    
        for _ in range(int(num/100)):
            roman += 'C'    
        num = num % 100    
        for _ in range(int(num/50)):
            roman += 'L'    
        num = num % 50   
        for _ in range(int(num/10)):
            roman += 'X'    
        num = num % 10    
        for _ in range(int(num/5)):
            roman += 'V'   
        num = num % 5  
        for _ in range(int(num/1)):
            roman += 'I'    
        num = num % 1  
            
		# cover edge cases manually
        roman = roman.replace('IIII', 'IV')
        roman = roman.replace('VIV', 'IX')
        roman = roman.replace('XXXX', 'XL')
        roman = roman.replace('LXL', 'XC')
        roman = roman.replace('CCCC', 'CD')
        roman = roman.replace('DCD', 'CM')
        
        return(roman)
        
        