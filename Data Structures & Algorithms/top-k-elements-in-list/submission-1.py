class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for n in nums:
            mp[n] += 1
        
        res = sorted(mp.keys(), key=lambda x: mp[x], reverse=True)
        return res[:k]