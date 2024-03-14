class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checker(n):
            hours = 0
            for i in range(len(piles)):
                hours += ceil(piles[i]/n)    
            return hours
        def helper(target):
            l = 1
            r = max(piles)
            while l <= r:
                mid = (l+r)//2
                if checker(mid)<=target:
                    r = mid - 1
                elif checker(mid)>target:
                    l = mid + 1
            return l
                
        return helper(h)
