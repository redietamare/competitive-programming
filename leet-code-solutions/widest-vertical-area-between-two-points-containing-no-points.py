class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x=[]
        for point in points:
            x.append(point[0])
        x.sort()
        maxx = 0
        for i in range(len(x)-1):
            maxx= max(x[i+1]-x[i],maxx)
        return maxx