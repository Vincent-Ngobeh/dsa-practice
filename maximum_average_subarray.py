class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]
        window_sum = sum(nums[:k])
        max_sub = window_sum
        left = 0
        right = k
        while right < len(nums):
            window_sum += nums[right]
            window_sum -= nums[left]
            max_sub = max(max_sub, window_sum)
            left+=1
            right+=1
        return max_sub/k
