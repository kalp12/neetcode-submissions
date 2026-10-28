class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (mask & b) > 0:
            # a sum without carry
            # b is carry with left shift 
            a, b = a ^ b, (a & b) << 1
        # if b is still greater than 0 than mask or take at most 3 else a
        return (mask & a) if b > 0 else a
