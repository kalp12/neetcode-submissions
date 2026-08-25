class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def dfs(curr, start, target):
            if target == 0:
                res.append(curr)
                return
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target: break
                dfs(curr + [candidates[i]], i + 1, target - candidates[i])
            return
        dfs([], 0, target)
        return res