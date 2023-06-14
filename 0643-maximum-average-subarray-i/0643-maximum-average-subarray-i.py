class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        windsum=sum(nums[:k])
        windav=float(f"{(windsum/k):.5f}")
        maxav=windav
        for end in range(k,len(nums)):
            windsum+=nums[end]
            windsum-=nums[end-k]
            average=windsum/k
            av=f"{average:.5f}"
            maxav=max(float(av),maxav)
        return(maxav)