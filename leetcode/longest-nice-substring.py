class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        maxlen = float("-inf")
        bol = False
        for i in range(len(s)):
            for j in range(i,len(s)):
                for k in s[i:j+1]:
                    if k.swapcase() not in s[i:j+1]:
                        break
                else:
                    bol = True
                    if len(s[i:j+1]) > maxlen:
                        maxlen = max(maxlen,len(s[i:j+1]))
                        ans = s[i:j+1]
        if bol == False:
            return ""
        return ans