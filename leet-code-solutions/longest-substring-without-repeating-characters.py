class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashset = defaultdict(int)
        maxlen = 0
        for r in range(len(s)):
            
            hashset[s[r]]+=1
            while hashset[s[r]]>1:
                hashset[s[l]] -= 1
                l += 1
            maxlen = max(maxlen,r-l+1)
        return maxlen