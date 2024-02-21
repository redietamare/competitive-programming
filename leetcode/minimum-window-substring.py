class Solution:
    def minWindow(self, s: str, t: str) -> str:
#         if t == "" : return ""
#         l = 0
#         t = Counter(t)
#         hashset = defaultdict(int)
#         minlen = float("inf")
#         have =0
#         need = len(t)
#         for r in range(len(s)):
#             hashset[s[r]] += 1
#             if s[r] in t and t[s[r]] == hashset[s[r]]:
#                 have += 1
#             while have == need:
#                 print(l)
#                 minlen = min(minlen,r-l+1)
#                 hashset[s[l]] -= 1
#                 if hashset[s[l]] in t and hashset[s[l]]<t[s[l]]:
#                     have -= 1
#                 l+=1
#         return minlen if minlen!=float("inf") else ""
    
    
    
    

        if t == "":
            return ""

        countT, window = Counter(t), defaultdict(int)


        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1 

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""