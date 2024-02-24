class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        #decreasing monotonic stack
        n = len(nums)
        nums= nums*2
        
        stack = []
        for i in range(len(nums)):
           
            
            while stack and nums[stack[-1]]<nums[i]:
                val = stack.pop()
                
                ans[val%n] = nums[i]
            stack.append(i)
            
        return ans