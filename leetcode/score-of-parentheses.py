class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score= 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            else:
                if stack:
                    stack.pop()
                    if s[i-1]=="(":
                        if len(stack)>=1:
                            score += 2**len(stack)
                        else: 
                            score += 1
        return score
                