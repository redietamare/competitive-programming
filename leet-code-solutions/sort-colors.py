class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        h0=0
        h2=len(nums)-1
        s=0
        while s<=h2:
            if nums[s]==0:
                nums[s],nums[h0]=nums[h0],nums[s]
                h0+=1
            elif nums[s]==2:
                nums[s],nums[h2]=nums[h2],nums[s]
                h2-=1
                s-=1
            s+=1
        return nums
                