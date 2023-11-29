class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        matrix=matrix[::-1]
        print(matrix)
        for i in range(len(matrix)-1):
            for j in range(1,len(matrix[i])):
                if matrix[i][j] != matrix[i+1][j-1]:
                    return False
        return True
                        
                
            