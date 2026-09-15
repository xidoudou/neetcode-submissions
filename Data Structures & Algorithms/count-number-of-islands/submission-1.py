class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0
            
        def dfs(grid, r, c, row, col):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == "0":
                return 
            grid[r][c] = "0"
            dfs(grid, r + 1, c, row, col)
            dfs(grid, r - 1, c, row, col)
            dfs(grid, r, c + 1, row, col)
            dfs(grid, r, c - 1, row, col)
        
        
        
        res = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    res += 1
                dfs(grid, i, j, row, col)
        return res

        
