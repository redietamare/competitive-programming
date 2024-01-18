class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        pre = 0
        ans = 0
        for i in nums:
            pre+=i
            diff= pre -goal
            ans+= count[diff]
            count[pre]+=1
        return ans