class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        seen = set()

        def dfs(i,j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0: return 1
            if (i, j) in seen: return 0

            seen.add((i, j))
            perim = dfs(i, j + 1)
            perim += dfs(i + 1, j)
            perim += dfs(i, j - 1)
            perim += dfs(i - 1, j)
            return perim

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    return dfs(i, j)