class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minn= float("inf")
        stack = []
        curmin = nums[0]
       
        for i in range(1,len(nums)):
            while stack and stack[-1][0]<=nums[i]:
                stack.pop()
            
            if stack and nums[i]>stack[-1][1] and  nums[i]<stack[-1][0]:
                return True
            
            stack.append((nums[i],curmin))
            curmin = min(curmin,nums[i])
        return False