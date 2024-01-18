class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0]*(len(nums)+1)
        for request in requests:
            prefix[request[0]] +=1
            prefix[request[1]+1] -= 1
        ans = []
        num =0
        for i in range(len(prefix)):
            num += prefix[i]
            ans.append(num)
        ans.sort(reverse = True)
        nums.sort(reverse = True)
        summ = 0
        for i in range(len(nums)):
            summ+=nums[i]*ans[i]
        
        return summ % (10**9 + 7)
            
        