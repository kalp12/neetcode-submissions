class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for n in t:
            d[n] += 1
        
        len_ans = float('inf')
        subl = subr = 0
        l = 0 
        r = 0
        formed = 0
        total = len(d)
        while r < len(s):
            char = s[r]
            if char in d:
                d[char] -= 1
                if d[char] == 0:
                    formed += 1

            while l <= r and formed == total:
                cur_len = r - l + 1
                if cur_len < len_ans:
                    len_ans = cur_len
                    subl = l
                    subr = r + 1
                
                char = s[l]
                if char in d:
                    if d[char] == 0:
                        formed -= 1
                    d[char] += 1
                l += 1
            r += 1
        return "" if formed == "inf" else s[subl: subr]