class Solution:
    def minPatches(self, nums: List[int], N: int) -> int:
        currsum = 0
        mincost = 0
        for n in nums:
            if n > N:
                break
            while n -1 > currsum:
                currsum += currsum + 1
                mincost += 1
            currsum += n
        while N > currsum :
            currsum += currsum + 1
            mincost += 1
        return mincost