class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_dif,cur_dif = 0,0
        for i in range(1,len(nums)):
            print(nums[0:i])

            cur_dif = (nums[i]-min(nums[0:i]))

            
            max_dif = max(max_dif,cur_dif)
        if max_dif == 0:
            max_dif = -1
        return(max_dif)