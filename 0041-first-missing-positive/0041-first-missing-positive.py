class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=1
        nums=set(nums)
        while i:
            if i not in nums:
                res=i
                break
            i+=1
        return(res)
        