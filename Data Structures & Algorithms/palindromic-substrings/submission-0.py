class Solution:
    def countSubstrings(self, s: str) -> int:
        counts = 0
        def pali(l, r):
            cnt = 0
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                cnt += 1
                l -= 1
                r += 1
            return cnt
        for i in range(len(s)):
            counts += pali(i, i)
            counts += pali(i, i + 1)
        return counts