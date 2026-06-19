class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for i, t in enumerate(tickets):
            if i <= k:
                res += min(t, tickets[k])
            else:
                res += min(t, tickets[k] - 1)
        return res