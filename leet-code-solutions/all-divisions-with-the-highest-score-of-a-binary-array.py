class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        hashmap=defaultdict(list)
        maxs = 0
        r0 = nums.count(0)
        r1 = nums.count(1)
        l0 = 0
        l1 = 0
        for i in range(len(nums)+1):
            if i-1>=0:
                if nums[i-1] == 0:
                    r0 -= 1
                    l0 +=1
                else:
                    r1 -= 1
                    l1 += 1
            maxs = l0 + r1
            hashmap[maxs].append(i)
        maxsum=max(hashmap.keys())
        return hashmap[maxsum]