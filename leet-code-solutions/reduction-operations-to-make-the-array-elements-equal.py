class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count=Counter(nums)
        nums = list(set(nums))
        nums.sort()
        ops = 0
     
        for i in range(1,len(nums)):
            ops += count[nums[i]]*i
        return ops
            
            