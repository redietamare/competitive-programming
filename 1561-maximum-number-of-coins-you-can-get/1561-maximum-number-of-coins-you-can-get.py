class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)//3
        sum=0
        for i in range(n):
            ind=-2+(i*(-2))
            sum+=piles[ind]
        return(sum)
        