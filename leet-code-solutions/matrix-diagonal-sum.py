class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ = 0
        rows = len(mat)
        cols = len(mat[0])
        tr = 0+ cols-1
        for i in range(rows):
            for j in range(cols):
                if i == j:
                    summ += mat[i][j]
                if (i+j == tr) and (i!=j):
                    summ += mat[i][j]
        return summ