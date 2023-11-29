class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        c=n
        while c>=1:
            for k in range(n-c+1):
                ans=s[k:c+k]
                if ans==ans[::-1]:
                    return ans
            c=c-1 