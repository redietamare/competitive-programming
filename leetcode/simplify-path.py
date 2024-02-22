class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        
        for i in path:
            if i!="" and i!="." and i !="..":
                stack.append(i)
            elif stack and i=="..":
                stack.pop()
        if stack:
            return "/"+"/".join(stack)
        else:
            return "/"