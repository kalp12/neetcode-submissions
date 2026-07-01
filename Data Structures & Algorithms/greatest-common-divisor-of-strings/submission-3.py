class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: return ""
        def greatcomondenominator(s1, s2):
            min_val = min(s1, s2)
            for i in range(min_val, 0, -1):
                if s1 % i == 0 and s2 % i == 0: return i
            return 1
        g = greatcomondenominator(len(str1), len(str2))
        return str1[:g]