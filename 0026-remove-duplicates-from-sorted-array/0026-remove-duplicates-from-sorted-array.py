class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        right=1
        left=0
        nums.sort()
        while right<len(nums):
            if nums[left]==nums[right]:
                nums.remove(nums[right])
            else:
                left+=1
                right+=1
        