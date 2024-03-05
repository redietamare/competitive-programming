class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans,buckets = [],[]
        candidates.sort()
        summ = 0
        def combs2(i):
            nonlocal summ
            if summ == target:
                ans.append(buckets.copy())
            val = None
            for j in range(i,len(candidates)):
                if val != candidates[j]:
                    buckets.append(candidates[j])
                    summ += candidates[j]
                    if summ <=target:
                        combs2(j+1)
                    val = buckets.pop()
                    summ-= val
        combs2(0)
        return ans