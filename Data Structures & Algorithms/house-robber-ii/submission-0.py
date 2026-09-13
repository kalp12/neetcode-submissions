class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(num):
            r1, r2 = 0, 0
            for n in num:
                r1, r2 = r2, max(r1 + n, r2)
            return r2
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))