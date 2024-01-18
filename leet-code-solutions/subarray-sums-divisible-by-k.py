class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre = 0
        ans = 0
        hashmap = defaultdict(int)
        hashmap[0]=1
        for i in nums:
            pre+=i
            # print(pre,hashmap)
            if (pre%k) in hashmap:
                ans+=hashmap[pre%k]
            hashmap[pre%k] += 1
            print(ans)
        return ans