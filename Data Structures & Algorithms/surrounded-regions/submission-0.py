class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        
        def dfs(r,c):
            if (r < 0 or c <0 or r >= row or c >= col or board[r][c] != "O"):
                return
            board[r][c] = "T"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        for r in range(row):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][col-1] == "O":
                dfs(r, col-1)
        
        for c in range(col):
            if board[0][c] == "O":
                dfs(0, c)
            if board[row-1][c] == "O":
                dfs(row-1, c)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        

