class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # monotonic increasing stack for finding the next and previous smaller element
        stack = [-1]
        summ = 0
        arr.append(0)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                val = stack.pop()
                l = val - stack[-1]
                r = i -val
                summ += l*r*arr[val]
            stack.append(i)
        return summ%(10**9 + 7)
            
                