class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        i = 0
        j = 0
        while i < n and j < m:
            start = i
            while i < n and j < m and haystack[i] == needle[j]:
                i += 1
                j += 1
            
            if j == m: return start
            i = start + 1
            j = 0
        return -1