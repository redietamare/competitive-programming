class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        score = 0
        l = 0
        maxscore = 0
        hashset =set()
        for r in range(len(nums)):
            score += nums[r]
            while nums[r] in hashset:
                hashset.remove(nums[l])
                score -= nums[l]
                l+=1
            maxscore = max(maxscore,score)
            hashset.add(nums[r])
        return maxscore