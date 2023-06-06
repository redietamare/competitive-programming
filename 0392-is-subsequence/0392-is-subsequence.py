class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps=0
        pt=0
        count=0
        while ps<=len(s)-1 and pt<=len(t)-1:
            if s and t:
                if s[ps]==t[pt]:
                    ps+=1
                    pt+=1
                    count+=1
                else:
                    pt+=1
            else:
                return(True)

        return(count==len(s))
