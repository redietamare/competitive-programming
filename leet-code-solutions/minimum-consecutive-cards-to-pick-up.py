class Solution:
    def minimumCardPickup(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        minlen = float("inf")
        for i in range(len(nums)):
            if nums[i] in hashmap:
                length = i - hashmap[nums[i]] + 1
                minlen = min(minlen,length)
            hashmap[nums[i]] = i
        if minlen == float("inf"):
            return -1
        else:
            return minlen
                