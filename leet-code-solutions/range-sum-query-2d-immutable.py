class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.prefix = []
        for i in range(self.rows+1):
            self.row = []
            for j in range(self.cols+1):
                self.row.append(0)
            self.prefix.append(self.row)
            
            
        for r in range(1,self.rows+1):
            self.pre = 0
            for c in range(1,self.cols+1):
                self.pre+=matrix[r-1][c-1]
                self.prefix[r][c]=self.pre + self.prefix[r-1][c]
        # print(self.prefix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # print(self.prefix[row2][col2])
        return self.prefix[row2+1][col2+1] -self.prefix[row2+1][col1] - self.prefix[row1][col2+1] + self.prefix[row1][col1] 

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)