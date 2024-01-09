class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        maxav=window/k
        for i in range(1,len(nums)-k+1):
            window-=nums[i-1]
            window+=nums[i+k-1]
            maxav=max(maxav,window/k)
        return(maxav)