class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [0]
        nums.insert(0,0)
        ans = []
        n = len(nums)
        pre = 0
        for i in range(1,len(nums)):
            pre+=nums[i]
            prefix.append(pre)
        for i in range(1,len(prefix)):
            x  = abs(prefix[i-1]-(nums[i]*(i-1)))
            y =abs(abs(prefix[n-1] - prefix[i-1]) - (nums[i]*(n-i)))
            ans.append(x+y)
        return ans