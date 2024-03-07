class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        def checker(div):
            result = 0
            for i in nums:
                result += ceil(i/div)
            return result
        def helper(l,r):
            while l <=r:
                mid = (l+r)//2
                if checker(mid) <= threshold:
                    r = mid -1
                else:
                    l = mid + 1
            return l
        return helper(l,r)