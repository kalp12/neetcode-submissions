class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def bt(i, path):
            if i == len(nums):
                res.append(path[::])
                return

            path.append(nums[i])
            bt(i + 1, path)
            path.pop()
            
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            bt(i + 1, path)
        bt(0, [])
        return res