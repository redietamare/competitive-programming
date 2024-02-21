class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        ans = list(palindrome)
        copy = list(palindrome)
        ind = -1
        if len(palindrome)==1 and "a":
            return ""
        for i in range(len(palindrome)):
            if palindrome[i] != "a":
                ans[i] = "a"
                ind = i
                break
        check = ans[::-1]
        if check == ans and ind != -1:
            copy[-1] = "b"
            return "".join(copy)
        if ind == -1:
            ans[-1]= "b"
        
        return "".join(ans)