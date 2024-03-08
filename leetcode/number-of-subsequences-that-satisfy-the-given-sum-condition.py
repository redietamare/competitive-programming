class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        ans = 0
        while l <= r:
            if nums[l] + nums[r]<=target:
                break
            else:
                r -= 1
  
        while l <= r:
            if nums[l] + nums[r] <=target:
                ans+= 2**(r-l)
                l+=1
            else:
                r-=1

        return ans %(10**9 + 7)