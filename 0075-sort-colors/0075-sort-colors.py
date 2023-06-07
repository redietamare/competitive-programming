class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder0=0
        holder2=len(nums)-1
        seeker=0
        while seeker<=holder2:
            if nums[seeker]==0:
                nums[seeker],nums[holder0]=nums[holder0],nums[seeker]
                holder0+=1
            elif nums[seeker]==2:
                nums[seeker],nums[holder2]=nums[holder2],nums[seeker]
                holder2-=1
                seeker-=1
            seeker+=1
        return(nums)


        

