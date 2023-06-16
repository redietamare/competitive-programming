class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return([])
        right=len(p)-1
        anagram=[]
        scount=Counter(s[0:len(p)-1])
        pcount=Counter(p)
        while right<len(s):
            scount[s[right]]+=1
            if scount==pcount:
                anagram.append(right-len(p)+1)
            scount[s[right-len(p)+1]]-=1
            if scount[s[right-len(p)+1]]==0:
                del scount[s[right-len(p)+1]]
            right+=1
        return(anagram)
            