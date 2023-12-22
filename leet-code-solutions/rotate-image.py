class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        swap=n
        for i in range(n//2):
            tl=[i,i]
            tr=[i,n-1-i]
            bl=[n-1-i,i]
            br=[n-1-i,n-1-i]
            for j in range(swap-1):
                matrix[tl[0]][tl[1]],matrix[tr[0]][tr[1]]=matrix[tr[0]][tr[1]],matrix[tl[0]][tl[1]]
                matrix[tl[0]][tl[1]],matrix[bl[0]][bl[1]]=matrix[bl[0]][bl[1]],matrix[tl[0]][tl[1]]
                matrix[bl[0]][bl[1]],matrix[br[0]][br[1]]=matrix[br[0]][br[1]],matrix[bl[0]][bl[1]]
                tl[0]+=1
                bl[1]+=1
                br[0]-=1
                tr[1]-=1
            swap-=2