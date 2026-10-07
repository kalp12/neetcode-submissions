class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        def dfs(r, c):
            grid[r][c] = 0
            lst = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in lst:
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "1": 
                    dfs(nr, nc)

        n = len(grid)
        m = len(grid[0])
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res