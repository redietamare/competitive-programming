class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trans = []
        for col in range(len(matrix[0])):
            newrow = []
            for row in range(len(matrix)):
                newrow.append(matrix[row][col])
            trans.append(newrow)
        return trans
                