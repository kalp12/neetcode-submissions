class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        dp = [False] * (n + 1)
        trues = [0]
        dp[0] = True
        for i in range(1, n + 1):
            for j in trues:
                if s[j:i] in wordDict:
                    dp[i] = True
                    trues.append(i)
                    break
        return dp[-1]