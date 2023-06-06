class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sbackspaced=[]
        tbackspaced=[]
        for i in s:
          
            if i=="#":
                if sbackspaced:
                    sbackspaced.pop()
            else:
                sbackspaced.append(i)
        for i in t:
            if i=="#":
                if tbackspaced:
                    tbackspaced.pop()
            else:
                tbackspaced.append(i)
        return(tbackspaced==sbackspaced)
