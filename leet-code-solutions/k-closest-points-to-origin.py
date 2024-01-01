class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashmap=defaultdict(list)
        for point in points:
            s=sqrt((point[0])**2 + (point[1])**2)
            hashmap[s].append(point)
        dis = sorted(hashmap.keys())
        ans = []
        
        for i in range(k):
            ans.extend(hashmap[dis[i]])
            if len(ans)==k:
                break
        return ans