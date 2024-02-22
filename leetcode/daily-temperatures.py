class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans = [0]*len(temp)
        #we use a monotonicly descreasing stack since we are trying to find a 
        stack = []
        for i in range(len(temp)):
            while stack and temp[stack[-1]]<temp[i]:
                val = stack.pop()
                ans[val] = i - val
            if not stack or temp[stack[-1]]>=temp[i]:
                stack.append(i)  
           
        return ans