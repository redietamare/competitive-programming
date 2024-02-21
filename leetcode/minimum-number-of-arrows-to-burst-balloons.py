class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[0])
        # print(points)
        arrows = 1
        minn = float("inf")
        i = 1
        while i<len(points):
            minn = min(minn,points[i-1][1])
            if points[i][0] > minn:
                arrows += 1
                minn = points[i][1]
                i += 1
            else:
                i+=1
        return arrows