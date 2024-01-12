class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        l = 0
        longest = 1
        for r in range(len(s)):
            hashmap[s[r]]+=1
            maxx = max(hashmap.values())
            while sum(hashmap.values())-maxx >k:
                hashmap[s[l]] -= 1
                l+=1
            longest = max(longest,r-l+1)
        return longest