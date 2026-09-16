class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        dp = [1, 1]             # two digits [0, 1] tens pos
        for i, n in enumerate(s[1:], 2):            # 2 because dp consists 2 and enumerate can start with that
            ways = 0
            if n != '0':
                ways += dp[i - 1]
            if 10 <= int(s[i - 2] + n) <= 26:
                ways += dp[i - 2]
            dp.append(ways)
        return dp[-1]