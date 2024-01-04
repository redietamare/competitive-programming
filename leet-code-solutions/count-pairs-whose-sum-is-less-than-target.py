class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # count=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]<target:
        #             count+=1
        # return count
        count=0
        nums.sort()
        l=0
        r=len(nums)-1
        while l<r:
            if nums[l]+nums[r]>=target:
                r-=1
            else:
                count+=r-l
                l+=1
        return count