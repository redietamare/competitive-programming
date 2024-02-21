class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        add = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            else:
                if not stack:
                    add += 1
                else:
                    stack.pop()
        if stack:
            add += len(stack)
        return add
                    