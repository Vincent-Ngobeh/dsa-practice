class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        # base cases
        dp = []
        dp.append(1)
        dp.append(2)
        count = 1
        ways = 0
        for i in range(2, n):
            ways = dp[i - 1] + dp[i-2]
            dp.append(ways)
        return dp[-1]
