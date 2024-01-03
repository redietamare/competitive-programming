class Solution:
    def isPalindrome(self, s: str) -> bool:
        z=''
        d=''
        lenn=len(s)
        for i in range(len(s)):
            if s[lenn-i-1].isalnum():
                z+=s[lenn-i-1].lower()
            if s[i].isalnum():
                d+=s[i].lower()
        return(z==d)
        