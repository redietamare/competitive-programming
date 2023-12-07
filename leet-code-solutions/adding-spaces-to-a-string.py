class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        newstr = ""
        p1=0
        i=0
        while i<len(s):
            if p1<len(spaces) and  i==spaces[p1]:
                newstr+=" "
                p1+=1
            else:
                newstr+=s[i]
                i+=1
        return newstr