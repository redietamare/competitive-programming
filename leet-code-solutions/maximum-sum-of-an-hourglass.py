class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        winds = rows + cols - 4
        maxsum = float("-inf")
        for i in range(rows-2):
            for j in range(cols-2):
                summ = 0
                summ += sum(grid[i][j:j+3])
                summ += grid[i+1][j+1]
                summ += sum(grid[i+2][j:j+3])
                maxsum = max(maxsum,summ)
                
        return maxsum