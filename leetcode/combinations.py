class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        buckets = []
        def combinations(i):
            if len(buckets)== k:
                ans.append(buckets.copy())
                return
            for j in range(i,n+1):
                buckets.append(j)
                combinations(j+1)
                buckets.pop()
        combinations(1)
        return ans
            