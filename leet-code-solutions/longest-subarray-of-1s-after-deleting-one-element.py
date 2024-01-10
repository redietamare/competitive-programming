class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        zero = 0
        longlen = 0
        for r in range(len(nums)):
            
            if nums[r] == 0:
                zero += 1
            # print(zero)
            while zero > 1:
                if nums[l] == 0:
                    zero -= 1
                l+=1
            longlen = max(longlen,r-l)
            # print(longlen)
        return longlen