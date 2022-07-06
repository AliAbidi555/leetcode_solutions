class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        closest_diff = 10000000
        closest_sum = 0
        nums.sort()
        if (x := sum(nums[:3])) >= target:
            return x
        if (x := sum(nums[-3:])) <= target:
            return x
        for left in range(length-2):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            mid = left + 1
            right = length - 1
            while mid < right:
                curr_sum = nums[left] + nums[mid] + nums[right]
                diff = abs(target-curr_sum)
                if diff < closest_diff:
                    closest_diff = diff
                    closest_sum = curr_sum
                if curr_sum < target:
                    mid += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return target
        return closest_sum