class Solution:
    def mySqrt(self, x: int) -> int:
        hi,low = x,0
        while hi >= low: 
            mid = (hi+low)//2
            if mid*mid > x: 
                hi = mid-1
            elif mid*mid < x: 
                low = mid + 1
            else:
                return(int(mid))
        return(hi)