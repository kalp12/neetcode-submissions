class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count

        # n = 101001001
        # n-1= 101001000
        # n-1= 101000111
        # ..

        # n & n - 1 removes that 1
        # n = 101001001
        # &
        # n-1= 101001000
        # 101001000