class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairsums = []
        for i in range(len(weights)-1):
            pairsums.append(weights[i]+weights[i+1])
        
        pairsums.sort()
        print(pairsums)
        mins = sum(pairsums[:k-1])
        maxx =sum(pairsums[n-k:])
        return maxx-mins