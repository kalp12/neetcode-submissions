class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = 0
        n = len(nums)
        last = n - 1
        for i in range(n):
            if right < i: return False
            if nums[i] + i > right: 
                right = nums[i] + i
            if right >= last: 
                return True