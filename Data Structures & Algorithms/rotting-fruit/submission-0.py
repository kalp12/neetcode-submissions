class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        rotten = []
        minutes = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))
        while rotten and fresh > 0:
            curr = []
            minutes += 1
            for r, c in rotten:
                for nr, nc in [(r + 1,c),(r - 1, c), (r , c + 1), (r, c - 1)]:
                    if nr >= 0 and nc >= 0 and nr < n and nc < m and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        curr.append((nr, nc))
                        if fresh == 0:
                            return minutes
                rotten = curr
        if fresh == 0: return minutes
        return -1