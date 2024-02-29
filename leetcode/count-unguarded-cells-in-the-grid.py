class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0]*n for i in range(m)]
        for g in guards:
            grid[g[0]][g[1]] = "G"
        for w in walls:
            grid[w[0]][w[1]]  = "W"
      
        for i in range(m):
            guarded = False
            for j in range(n):
                if grid[i][j] == "G":
                    guarded = True
                elif grid[i][j] =="W":
                    guarded = False
                elif guarded:
                    grid[i][j] = "N"
            guarded = False
            for j in range(n-1,-1,-1):
                if grid[i][j] == "G":
                    guarded = True
                elif grid[i][j] =="W":
                    guarded = False
                elif guarded:
                    grid[i][j] = "N"
            
        for j in range(n):
            guarded = False
            for i in range(m):
                if grid[i][j] == "G":
                    guarded = True
                elif grid[i][j] =="W":
                    guarded = False
                elif guarded:
                    grid[i][j] = "N"
            guarded = False
            for i in range(m-1,-1,-1):
                if grid[i][j] == "G":
                    guarded = True
                elif grid[i][j] =="W":
                    guarded = False
                elif guarded:
                    grid[i][j] = "N"
        
        c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    c+=1
        return c