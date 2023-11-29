class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=str(x)
        numm=num[::-1]
        return numm==num