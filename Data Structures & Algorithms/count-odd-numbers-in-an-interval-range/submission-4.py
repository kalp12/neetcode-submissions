class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = high - low + 1
        cnt = length // 2
        if length % 2 and low % 2:
            cnt += 1
        return cnt