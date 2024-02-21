class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        triplets = 0
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            a = nums[i]

            r = i-1
            for l in range(i-1):
                while l<r and nums[l] + nums[r] > a:
                    r -= 1
                if l < r:
                    triplets += i-r-1
                else:
                    triplets += i - l - 1
        return triplets
        