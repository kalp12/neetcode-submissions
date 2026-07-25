class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        res = 0
        for n in nums:
            res += cnt[n]
            cnt[n] += 1
        return res