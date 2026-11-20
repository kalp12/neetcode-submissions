class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        vis = set()
        h = [[grid[0][0], 0, 0]]        # minheap (time/ max(height), r, c)
        d = [[1, 0],[0, 1], [-1, 0], [0, -1]]

        vis.add((0,0))
        while h:
            t, r, c = heapq.heappop(h)
            if r == n - 1 and c == n - 1: return t
            for dr, dc in d:
                nr, nc = dr + r, dc + c
                if (nr < 0 or nc < 0 or nr == n or nc == n or (nr, nc) in vis): continue
                vis.add((nr, nc))
                heapq.heappush(h, [max(t, grid[nr][nc]), nr, nc])