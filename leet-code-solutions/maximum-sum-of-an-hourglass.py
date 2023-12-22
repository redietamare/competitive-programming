class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        winds = rows + cols - 4
        maxsum = float("-inf")
        for i in range(rows-2):
            for j in range(cols-2):
                summ = 0
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        summ+=grid[r][c]
                summ-=grid[i+1][j]
                summ-=grid[i+1][j+2]
                maxsum = max(maxsum,summ)
        return maxsum