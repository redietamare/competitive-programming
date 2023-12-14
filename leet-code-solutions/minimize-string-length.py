class Solution:
    def minimizedStringLength(self, s: str) -> int:
        count=Counter(s)
        n=len(s)
        for i in count:
            if count[i]>1:
                n-=(count[i]-1)
        return n