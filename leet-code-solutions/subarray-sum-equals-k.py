class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap=defaultdict(int)
        hashmap[0]=1
        presum=0
        res=0
        for i in nums:
            presum+=i
            diff=presum-k
            res+=hashmap[diff]
            hashmap[presum]+=1
            
        return res