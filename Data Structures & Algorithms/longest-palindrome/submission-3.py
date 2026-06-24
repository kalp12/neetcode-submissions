class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        res = 0
        for n in s:
            if n in seen:
                seen.remove(n)
                res += 2
            else:
                seen.add(n)
        
        return res + 1 if seen else res