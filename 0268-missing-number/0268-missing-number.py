class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        newlist=[]
        for i in range(n+1):
            newlist.append(i)
        for i in newlist:
            if i not in nums:
                return(i)
