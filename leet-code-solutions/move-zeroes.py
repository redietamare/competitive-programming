class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        h=0
        s=0
        while s<len(nums):
            if nums[s]!=0:
                nums[s],nums[h]=nums[h],nums[s]
                h+=1
            s+=1
        
        