class Solution:
    def printVertically(self, s: str) -> List[str]:
        maxlen=0
        s=s.split()
        
        for i in s:
            if len(i)>maxlen:
                maxlen=len(i)
        ans=[""]*maxlen
        dic=defaultdict(str)
        for i in range(maxlen):
            for j in range(len(s)):
                if i>=len(s[j]):
                    ans[i]+=" "
                else:
                    ans[i]+=s[j][i]
                
        return [i.rstrip() for i in ans]