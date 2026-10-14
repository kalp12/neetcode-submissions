class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        def capture(r, c):
            if r < 0 or r == n or c < 0 or c == m or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # capture boundary with O
        for i in range(n):
            for j in range(m):
                if (
                    board[i][j] == "O" and ( i in [0, n - 1] or j in [0, m - 1])
                ):
                    capture(i, j)

        # convert rest O to x
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
        # convert t with O
        for i in range(n):
            for j in range(m):
                if board[i][j] == "T":
                    board[i][j] = "O"