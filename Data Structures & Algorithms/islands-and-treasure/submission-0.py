class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        vis = set()

        def addroom(r, c):
            if (r < 0 or r == n or c < 0 or c == m or (r, c) in vis or grid[r][c] == -1): return 
            vis.add((r, c))
            q.append((r, c))

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    q.append((r, c))
                    vis.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addroom(r - 1, c)
                addroom(r + 1, c)
                addroom(r, c - 1)
                addroom(r, c + 1)
            dist += 1