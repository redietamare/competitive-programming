class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in range(len(s)):
            if s[i].isalnum():
                string+=s[i]
        st = string.lower()
        l=0
        r=len(st)-1
        while l<=r:
            if st[l]!=st[r]:
                return False
            r-=1
            l+=1
        return True