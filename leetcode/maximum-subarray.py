class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # largest=float("-inf")
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         largest=max(sum(nums[i:j+1]),largest)
        # return largest
        # largest=float("-inf")
        # for i in range(len(nums)):
        #     runsum=0
        #     for j in range(i,len(nums)):
        #         runsum+=nums[j]
        #         largest=max(runsum,largest)
        # return largest
        largest=nums[0]
        presum=0
        for i in nums:
            presum+=i
            largest=max(presum,largest)
            if presum<0:
                presum=0

        return largest
                