class Solution:
    def partitionString(self, s: str) -> int:
        unique=""
        string=[]
        left=0
        while left<len(s)-1:
            unique+=s[left]
            if s[left+1] in unique:
                string.append(unique)
                unique=""
            left+=1
        string.append(s[left-1:])
        return(len(string))

