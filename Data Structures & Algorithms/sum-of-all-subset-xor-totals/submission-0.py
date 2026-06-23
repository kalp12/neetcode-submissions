class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, tot):
            if i == len(nums):
                return tot
            return dfs(i + 1, tot ^ nums[i]) + dfs(i + 1, tot)
        return dfs(0,0)