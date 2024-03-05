class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans ,buckets = [],[]
        summ = 0
        nums = [i for i in range(1,10)]
     
        def combs3(i):
            nonlocal summ
            if summ == n and len(buckets)==k and buckets.copy() not in ans:
                ans.append(buckets.copy())
            for j in range(i,len(nums)):
                buckets.append(nums[j])
                summ += nums[j]
                if summ <= n:
                    combs3(j+1)
                val = buckets.pop()
                summ -= val
            
        combs3(0)
        return ans
