class Solution:
    def countBits(self, n: int) -> List[int]:
        count = []
        for i in range(n + 1):
            count.append(i.bit_count())
        return count