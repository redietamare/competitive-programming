class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n=len(nums)
        hashmap = {0:-1}
        pre = 0
        rem = sum(nums)%p
        ans = float("inf")
        if rem == 0:
            return 0
        for i in range(n):
            pre+=nums[i]
            k = (pre%p - rem)%p
            if k in hashmap:
                ans = min(ans,i-hashmap[k])
            hashmap[pre%p] = i
        if ans<n:
            return ans
        return -1
