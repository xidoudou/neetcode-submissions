from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        fresh_count = 0
        rotten = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    rotten.append([i, j])

        def turnRotten(r, c):
            nonlocal fresh_count
            if (r >= 0 and r < row and c >= 0 and c < col and grid[r][c] == 1):
                grid[r][c] = 2
                fresh_count -= 1
                rotten.append([r, c])

        time = 0
        while rotten and fresh_count > 0:
            for i in range(len(rotten)):
                r, c = rotten.popleft()
                turnRotten(r-1, c)
                turnRotten(r+1, c)
                turnRotten(r, c+1)
                turnRotten(r, c-1)
            time += 1

        return time if fresh_count == 0 else -1