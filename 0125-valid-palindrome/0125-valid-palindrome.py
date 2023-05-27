class Solution:
    def isPalindrome(self, s: str) -> bool:
        listt=[]
        for i in s:
            if i.isalnum():
                if i==i.upper():
                    listt.append(i.lower())
                else:
                    listt.append(i)
        return listt==list(reversed(listt))