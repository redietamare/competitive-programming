class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        sumleft = defaultdict(int)
        countleft = defaultdict(int)
        resleft = [0]*len(nums)
        for i,x in enumerate(nums):
            resleft[i] += countleft[x]*i
            resleft[i] -= sumleft[x]

            countleft[x] += 1
            sumleft[x] += i
        
        sumright = defaultdict(int)
        countright = defaultdict(int)
        nums.reverse()
        resright = [0]*len(nums)
        for i,x in enumerate(nums):
            resright[i] += countright[x]*i
            resright[i] -= sumright[x]

            countright[x] += 1
            sumright[x] += i
        print(resright)
        resright.reverse()
        res = []
        for i in range(len(resleft)):
            res.append(resleft[i]+resright[i])
        return res