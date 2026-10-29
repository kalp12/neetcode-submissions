class Solution:
    def reverse(self, x: int) -> int:
        mn = -2 ** 31
        mx = 2 ** 31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x:
            digit = (x % 10)
            rev = rev * 10 + digit
            x //= 10
        if rev < mn or rev > mx:
            return 0
        return rev * sign