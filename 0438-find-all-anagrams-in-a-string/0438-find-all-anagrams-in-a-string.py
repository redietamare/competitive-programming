class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left=0
        right=len(p)
        strr=list(s)
        output=[]
        pcount=Counter(p)
        while right<=len(s):
            scount=Counter(s[left:right])
            if scount==pcount:
                output.append(left)
            left+=1
            right+=1
        return(output)
        
            
            
        
        