class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        val1=float("inf")
        val2=float("inf")
        for num in nums:
            if num<=val2 and num>val1:
                val2=num
            elif num<=val1:
                val1=num
            if num>val2 and num>val1:
                return True
        return False