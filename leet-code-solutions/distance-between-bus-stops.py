class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s = min(start,destination)
        d = max(start,destination)
        dis_1 = 0
        whole_path = sum(distance)
        for i in range(s,d):
            dis_1 += distance[i]
        return min(dis_1 , whole_path-dis_1)