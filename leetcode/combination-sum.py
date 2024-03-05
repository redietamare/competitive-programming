class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans , buckets = [] , []
        summ = 0
        
        def comb(i):
            nonlocal summ
            if summ ==  target:
                ans.append(buckets.copy())
            for j in range(i,len(candidates)):
                buckets.append(candidates[j])
                summ += candidates[j]
                if summ <= target:
                    comb(j)
                val = buckets.pop()
                summ -= val
        comb(0)
        return ans