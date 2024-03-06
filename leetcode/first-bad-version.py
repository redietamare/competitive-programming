# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        h = n
        while l<=h:
            mid = (l+h)//2
            if isBadVersion(mid) == True and isBadVersion(mid-1) == False:
                return mid
            elif isBadVersion(mid) == True and isBadVersion(mid-1) == True:
                h = mid - 1 
            elif isBadVersion(mid) == False:
                l = mid + 1
