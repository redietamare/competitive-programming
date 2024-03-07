class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        maxx = float("-inf")
        heaters.sort()
        for i in range(len(houses)):
            minn = float("inf")
            l = 0
            r = len(heaters) - 1
            while l<=r:
                mid = (l+r)//2
                if houses[i] < heaters[mid]:
                    minn = min(minn,abs(houses[i]-heaters[mid]))
                    r = mid-1
                else:
                    minn = min(minn,abs(houses[i]-heaters[mid]))
                    l = mid + 1
            maxx = max(minn,maxx)
        return maxx
