class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        summ=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i+1]+=1
                summ+=1
            if nums[i]>nums[i+1]:
                c=nums[i]-nums[i+1]
                nums[i+1]=nums[i+1]+c+1
                summ+=c+1
        return(summ)
        