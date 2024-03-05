class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        buckets = []
        def subset(i):
            if len(buckets) <= len(nums):
                ans.append(buckets.copy())
                
            for j in range(i,len(nums)):
                
                buckets.append(nums[j])
               
                subset(j+1)
                buckets.pop()
               
        subset(0)
        return ans