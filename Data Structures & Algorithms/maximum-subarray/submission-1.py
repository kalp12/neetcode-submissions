class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        curr = nums[0]
        for n in nums[1:]:
            curr = max(n, n + curr)
            mx = max(mx, curr)
        return mx