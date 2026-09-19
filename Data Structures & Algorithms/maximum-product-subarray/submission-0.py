class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_p = max_p = nums[0]
        max_product = max_p
        for num in nums[1:]:
            tmp = min_p
            min_p = min(num, num * min_p, num * max_p)
            max_p = max(num, num * tmp, num * max_p)
            max_product = max(max_product, max_p)
        return max_product