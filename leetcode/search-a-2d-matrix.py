class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = []
       
        for i in matrix:
            l.extend(i)
        n=len(l)
        # print(l,bisect_left(l,target),l[bisect_left(l,target)])
        if bisect_left(l,target) < n and l[bisect_left(l,target)]==target:
            return True
        return False