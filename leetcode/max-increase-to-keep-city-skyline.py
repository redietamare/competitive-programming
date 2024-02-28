class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        summ = 0
        rows = len(grid)
        cols = len(grid[0])
        rowmax = []
        colmax = []
        for i in range(rows):
            maxx = float("-inf")
            for j in range(cols):
                maxx = max(maxx,grid[i][j])
            rowmax.append(maxx)
        for j in range(cols):
            maxx = float("-inf")
            for i in range(rows):
                maxx = max(maxx,grid[i][j])
            colmax.append(maxx)
        for i in range(rows):
            for j in range(cols):
                val = min(rowmax[i],colmax[j])
                summ += abs(val-grid[i][j])
        return summ