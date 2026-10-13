class Solution:
    def check(self, r, c, heights, ocean):
        ocean[r][c] = True
        lst = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for nr, nc in lst:
            if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and not ocean[nr][nc] and heights[nr][nc] >= heights[r][c]:
                self.check(nr, nc, heights, ocean)
        return 

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        res = []
        atl = [[False for _ in range(cols)] for _ in range(rows)]
        pac = [[False for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            self.check(r, 0, heights, pac)
            self.check(r, cols - 1, heights, atl)
        for c in range(cols):
            self.check(0, c, heights, pac)
            self.check(rows - 1, c, heights, atl)

        for r in range(rows):
            for c in range(cols):
                if atl[r][c] and pac[r][c]:
                    res.append([r,c])
        return res