def get_maximum(nums):
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[1], nums[0]))
        maximum_amount = 0
        for i in range(2, len(nums)):
           maximum_amount = max(nums[i] + dp[i-2], dp[i-1])
           dp.append(maximum_amount)
        return dp[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[1], nums[0])
        return max(get_maximum(nums[0:len(nums)-1]), get_maximum(nums[1:len(nums)]))
