class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == "":
            return True

        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for word in wordDict:
                if i - len(word) >= 0 and dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
        return dp[i]
