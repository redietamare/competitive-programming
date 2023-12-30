class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        summ=count=0
        for i in costs:
            summ+=i
            if summ<=coins:
                count+=1
        return count