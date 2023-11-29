class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=str(x)
        numm=num[::-1]
        return numm==num
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # s=str(x)
        # revstr=""
        # for i in range(len(s)):
        #     revstr+=s[len(s)-i-1]
        # if revstr==s:return True
        # else: return False