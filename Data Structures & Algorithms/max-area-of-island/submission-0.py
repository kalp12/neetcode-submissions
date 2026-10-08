class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mx = 0
        def dfs(r, c):
            num = 1
            grid[r][c] = 0
            lst = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for nr, nc in lst:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    num += dfs(nr, nc)
            return num 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    mx = max(mx, dfs(i, j))
        return mx