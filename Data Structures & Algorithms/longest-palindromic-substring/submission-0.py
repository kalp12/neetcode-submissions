class Solution:
    def isPali(self, st, left, right):
        while left > 0 and right < len(st) - 1 and st[left - 1] == st[right + 1]:
            left -= 1
            right += 1
        return left, right, right - left + 1

    def longestPalindrome(self, s: str) -> str:
        left, right, max_len = 0, 0, 0
        for i in range(len(s) - 1):
            # middle
            l1, r1, max_len1 = self.isPali(s, i, i)
            if max_len1 > max_len:
                max_len = max_len1
                left, right = l1, r1
            
            # between middle
            if s[i] == s[i + 1]:
                l2, r2, max_len2 = self.isPali(s, i, i + 1)
                if max_len2 > max_len:
                    max_len = max_len2
                    left, right = l2, r2
        return s[left: right + 1]