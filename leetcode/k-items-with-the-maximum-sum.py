class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # arr = []
        # for i in range(numOnes):
        #     arr.append(1)
        # for i in range(numZeros):
        #     arr.append(0)
        # for i in range(numNegOnes):
        #     arr.append(-1)
        # arr.sort(reverse = True)
        # summ=0
        # for i in range(k):
        #     summ+=arr[i]
        # return summ
        if k<= numOnes:
            return k
        elif k<=numOnes + numZeros:
            return numOnes
        else:
            return numOnes - (k-(numOnes + numZeros))