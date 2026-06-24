class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = defaultdict(int)
        res = 0
        for n in s:
            mp[n] += 1
            if mp[n] % 2 == 0:
                res += 2
        
        for cnt in mp.values():
            if cnt % 2 == 1:
                res += 1
                break
        return res