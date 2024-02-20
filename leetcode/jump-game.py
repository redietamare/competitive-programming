class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxx = 0
        for i in range(len(nums)-1):
            maxx = max(maxx-1,nums[i])
            if maxx<=0:
                return False
        return True
    