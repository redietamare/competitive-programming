class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        #mono increasing stack
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if i in stack:
                    counter[i] -= 1
                    continue
                while stack and stack[-1]>i and counter[stack[-1]]>1:
                    val=stack.pop()
                    counter[val]-=1
                stack.append(i)
        return "".join(stack)
            
            
            
            
            
