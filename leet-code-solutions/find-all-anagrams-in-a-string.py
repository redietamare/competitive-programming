class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp = len(p)
        cp = Counter(p)
        win =Counter(s[:lp-1])
        ans = []
        for i in range(len(s)-lp+1):
            win[s[i+lp-1]]+=1
            if win == cp:
                ans.append(i)
            win[s[i]]-=1
        return ans