class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        freq = 0 
        val = 1
        ans = []
        while val <= len(nums):
            vals = [nums[val]] * nums[freq]
            ans.extend(vals)
            freq += 2
            val += 2
        return ans