class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        good = 0
        odd = 0
        count =0
        for r in range(len(nums)):
            if nums[r]%2==1:
                odd+=1
                count = 0
            while odd==k:
                if nums[l]%2==1:
                    odd-=1
                l+=1
                count += 1 
            print(nums[r],count,l)
            good += count
        return good