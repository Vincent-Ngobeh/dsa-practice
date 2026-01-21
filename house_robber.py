class Solution:
    def rob(self, nums: List[int]) -> int:
       if len(nums) == 0:
          return 0
       if len(nums) == 1:
          return nums[0]
       if len(nums) == 2:
          return max(nums[1], nums[0])

       # Base cases
       dp = []
       dp.append(nums[0])
       dp.append(max(nums[1], nums[0]))

       #recursive case
       for i in range(2, len(nums)):
            current_max = max(nums[i] + dp[i-2], dp[i-1])
            dp.append(current_max)
       return dp[-1]
