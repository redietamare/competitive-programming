class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        preleft = []
        prel = 0
        for i in nums:
            prel += i
            preleft.append(prel)
        nums = nums[::-1]
        prer = 0
        preright = []
        for i in nums:
            prer += i
            preright.append(prer)
        preright = preright[::-1]
        for i in range(len(preleft)):
            if preleft[i]==preright[i]:
                return i
        return -1