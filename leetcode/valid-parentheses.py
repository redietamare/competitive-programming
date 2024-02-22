class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
                    "}":"{",
                   ")":"(",
                   "]":"["    
                }
        stack = []
        for i in s:
            if i == "(" or i == "[" or i=="{":
                stack.append(i)
            else:
                if stack and stack[-1] == hashmap[i]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True