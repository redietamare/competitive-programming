class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a = b = len(costs)/2
        total = 0
        costs.sort(key = lambda x:abs(x[0]-x[1]) ,reverse = True)
        print(costs)
        for acost,bcost in costs:
            if b==0 or (a and acost <= bcost):
                total += acost
                a -=1
            else:
                total += bcost
                b -= 1
        return total