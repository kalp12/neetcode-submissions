class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        res = 0
        for p in prices[1:]:
            res = max(res, p - mn)
            mn = min(mn, p)
        return res