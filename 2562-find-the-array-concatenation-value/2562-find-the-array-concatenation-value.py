class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        numstr=deque(nums)
        conc=0
        left=0
        right=len(numstr)-1
        while numstr:
            if len(numstr)>1:
                conc+=int(numstr[0]+numstr[-1])
                numstr.popleft()
                numstr.pop()
            else:
                conc+=int(numstr[0])
                break
        return(conc)