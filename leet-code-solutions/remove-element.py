class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i]==val:
                nums[i]="_"
        h=s=0
        while s<len(nums):
            if nums[s]!="_":
                nums[s],nums[h]=nums[h],nums[s]
                h+=1
            s+=1
        # print(nums)
        ind = len(nums)
        for i in range(len(nums)):
            if nums[i]=="_":
                ind=i
                break
    
        return len(nums[:ind])
            