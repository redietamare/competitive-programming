class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        summ=0
        j=0
        for i in range(len(piles)//3):
            summ+=piles[-2-j]
            j+=2
        return summ