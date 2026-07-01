class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: return ""
        def greatcomondenominator(s1, s2):
            while s2:
                s1, s2 = s2, s1 % s2
            return s1
        g = greatcomondenominator(len(str1), len(str2))
        return str1[:g]