class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        summ = 0
        minlen = float("inf")
        for r in range(len(nums)):
            summ += nums[r]
            while summ>= target:
                minlen = min(minlen,r - l + 1)
                summ -= nums[l]
                l += 1
    
        if minlen == float("inf"):
            return 0
        else: return minlen