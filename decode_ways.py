class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if not s:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1  # empty string: one way to decode nothing

        # dp[1] = first character
        if int(s[0]) >= 1 and int(s[0]) <= 9:
            dp[1] = 1

        for i in range(2, n + 1):
            # consume 1 character: s[i-1]
            if int(s[i-1]) >= 1 and int(s[i-1]) <= 9:
                dp[i] += dp[i-1]

            # consume 2 characters: s[i-2]+s[i-1]
            if int(s[i-2] + s[i-1]) >= 10 and int(s[i-2] + s[i-1]) <= 26:
                dp[i] += dp[i-2]

        return dp[n]
