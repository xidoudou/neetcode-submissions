class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        visit = set()
        q = deque()
        
        def addRoom(r,c):
            if (r < 0 or 
                c < 0 or 
                r == row or 
                c == col or 
                grid[r][c]== -1 or 
                (r,c) in visit):
                return
            q.append([r,c])
            visit.add((r,c))
            

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visit.add((i,j))
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r, c+1)
                addRoom(r, c-1)

            dist += 1
            
        

        