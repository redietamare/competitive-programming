class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        ## checking rows
        for i in range(rows):
            sett = set()
            for j in range(cols):
                if board[i][j] in sett:
                    
                    return False
                if board[i][j]!=".":
                    sett.add(board[i][j])
        ##checking cols
        for j in range(cols):
            sett = set()
            for i in range(rows):
                if board[i][j] in sett:
                    return False
                if board[i][j]!=".":
                    sett.add(board[i][j])   
        ##checking squares
        for i in range(0,rows,3):
            for j in range(0,cols,3):
                sett = set()
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        if board[r][c] in sett:
                            return False
                        if board[r][c]!=".":
                            sett.add(board[r][c])
        return True
            