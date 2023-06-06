class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        right=len(s)-1
        left=0
        s=list(s)
        count=0
        while right>=left:
            if ord(s[left])>ord(s[right]):
                s[left]=s[right]
                count+=1
            elif ord(s[left])<ord(s[right]):
                s[right]=s[left]
                count+=1
            left+=1
            right-=1
        return("".join(s))