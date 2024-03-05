class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        buckets = []
        def subset2(i):
            if len(buckets) <=len(nums):
                if buckets.copy() not in ans:
                    ans.append(buckets.copy())
            for j in range(i,len(nums)):
                buckets.append(nums[j])
                subset2(j+1)
                buckets.pop()
        subset2(0)
        return ans