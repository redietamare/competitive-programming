class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr=[]
        for i in range(len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
                arr.append(j)
        arr=set(arr)
        for i in range(left,right+1):
            if i not in arr:
                return False
        return True