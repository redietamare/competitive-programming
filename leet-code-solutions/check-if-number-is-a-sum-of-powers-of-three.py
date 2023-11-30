class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        arr=[]
        for i in range(17):
            arr.append(3**i)
        for i in range(17):
            comb=list(combinations(arr,i))
            for j in comb:
                if sum(j)==n:
                    return True
        return False
        