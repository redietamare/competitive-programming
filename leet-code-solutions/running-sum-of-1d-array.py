class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        runsum = 0
        for i in range(len(nums)):
            runsum+=nums[i]
            ans.append(runsum)
        return ans