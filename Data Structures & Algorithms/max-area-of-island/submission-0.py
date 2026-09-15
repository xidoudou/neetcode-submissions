class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            return (1 + dfs(r - 1, c)+
                        dfs(r + 1, c)+
                        dfs(r, c + 1)+
                        dfs(r, c - 1))
        
        maxArea = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                maxArea = max(maxArea, dfs(i,j))
        return maxArea
                
        