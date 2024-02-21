class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix = [0]
        pre = 0
        for i in nums:
            pre += i
            prefix.append(pre)
        maxx = float("-inf")
        for i in range(1,len(prefix)):
            maxx = max(maxx,ceil(prefix[i]/i))
        return maxx