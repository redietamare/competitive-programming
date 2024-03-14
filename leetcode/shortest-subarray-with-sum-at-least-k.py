class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # l = 0
        # summ = 0
        # minlen = float("inf")
        # for r in range(len(nums)):
           
        #     summ += nums[r]
        #     print(summ)
        #     while summ >= k:
        #         minlen = min(minlen,r-l+1)
        #         summ -= nums[l]
        #         l += 1
        #         print(summ,l,minlen)
        # if minlen == float("inf"):
        #     return -1
        # return minlen
        queue = deque()
        pre = [0]
        for i in nums:
            pre.append(pre[-1]+i)
        minlen = float("inf")
        for i in range(len(pre)):
          
            while queue and queue[-1][0]>=pre[i]:
                queue.pop()
            queue.append((pre[i],i))
            while queue and pre[i]-queue[0][0]>=k:
                minlen = min(i-queue[0][1],minlen)
                queue.popleft()
            
        if minlen == float("inf"):
            return -1
        return minlen


