class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numsSet = set(nums)
        for n in numsSet:
            if (n - 1) not in numsSet:
                length = 0
                while (length + n) in numsSet:
                    length += 1
                res = max(length, res)

        return res