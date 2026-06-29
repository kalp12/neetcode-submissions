class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mp = Counter(arr)
        res = -1
        for n in mp:
            if n == mp[n]:
                res = max(res, n)
        return res