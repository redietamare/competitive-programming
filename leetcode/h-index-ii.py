class Solution:
    def hIndex(self, c: List[int]) -> int:
        n =  len(c)
        l = 0
        r = n - 1
        while l <= r:
            mid = (l+r)//2
            if c[mid] >= n-mid:
                r = mid - 1
            else:
                l = mid + 1
        return n - l