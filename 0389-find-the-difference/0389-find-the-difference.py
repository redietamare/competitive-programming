class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        strs=list(s)
        strt=list(t)
        for i in strs:
            if i in strt:
                strt.remove(i)
        for i in strt:
            return(i)
        
        