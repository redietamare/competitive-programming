class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        maxx = trips[0][2]
        ans = []
        for trip in trips:
            maxx = max(maxx,trip[2])
        prefix=[0]*(maxx+2)
        for trip in trips:
            st = trip[1]
            ep = trip[2]
            pas = trip[0]
            prefix[st] += pas
            prefix[ep]-=pas
        pre = 0
        for i in range(len(prefix)-1):
            pre+=prefix[i]
            ans.append(pre)
        maxx = max(ans)
        return capacity>=maxx
        