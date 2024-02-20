class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        ans = []
        for i in range(len(s)-1,-1,-1):
            if s[i] not in hashmap:
                hashmap[s[i]] = i
        # print(hashmap)
        ind = l = 0
        for r in range(len(s)):
            ind = max(ind,hashmap[s[r]])
            if r == ind:
                ans.append(r-l+1)
                l = r+1
        return ans