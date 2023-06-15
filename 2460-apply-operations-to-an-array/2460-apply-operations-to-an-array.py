class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        right=1
        left=0
        while right<len(nums):
            if nums[left]==nums[right]:
                nums[left]=nums[left]*2
                nums[right]=nums[right]*0
            right+=1
            left+=1
        seeker=0
        holder=0
        while seeker<len(nums):
            if nums[seeker]!=0:
                nums[holder],nums[seeker]=nums[seeker],nums[holder]
                holder+=1
            seeker+=1
        return(nums)