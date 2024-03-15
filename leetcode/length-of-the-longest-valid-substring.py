class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        maxfblen = float("-inf")
        setfb = set(forbidden)
        for i in forbidden:
            maxfblen = max(maxfblen,len(i))
        n = len(word)
        def validity(left, right):
            left = max(left - 1, right - maxfblen)
            for i in range(right, left, -1):
                if word[i:right+1] in setfb:
                    return False
            
            return True
        l = 0   
        maxlen = float("-inf") 
        for r in range(len(word)):
            valid= True
            # val = validity(l,r)
            while l<n and not validity(l,r):
                l += 1
            maxlen = max(maxlen,r-l+1)
        if maxlen == float("-inf"):
            return 0
        return maxlen

