class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                ind = i
                while i<len(nums)-1 and nums[i+1]==nums[ind]:
                    nums[i+1]="_"
                    i+=1
            else:
                i+=1
        h=s=0
        while s<len(nums):
            if nums[s]!="_":
                nums[h],nums[s]=nums[s],nums[h]
                h+=1
            s+=1
        for i in range(len(nums)):
            if nums[i]=="_":
                break
            a = i
        return len(nums[:a+1])

                
                
                
                
                