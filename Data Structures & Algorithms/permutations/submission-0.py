class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(path, used):
            if len(path) == n:
                res.append(path[:])
                return 
            
            for i in range(n):
                if used[i]: continue
                used[i] = True
                path.append(nums[i])

                dfs(path, used)
                path.pop()
                used[i] = False
            
        dfs([], [False] * n)
        return res