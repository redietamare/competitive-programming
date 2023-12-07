class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        summ=0
        for i in range(len(points)-1):
            if points[i][0]*points[i+1][0]>=0:
                a=abs(points[i][0]-points[i+1][0])
            else:
                a= abs(points[i][0]) + abs(points[i+1][0])
            if points[i][1]*points[i+1][1]>=0:
                b=abs(points[i][1]-points[i+1][1])
            else:
                b= abs(points[i][1]) + abs(points[i+1][1])
            summ+=max(a,b)
        return summ