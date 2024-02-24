class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for num in tokens:
            if num.isdigit()or (num[0]=="-" and len(num)>1):
                stack.append(int(num))
            else:
                y = stack.pop()
                x = stack.pop()
               
                if num =="+":
                    val =  x + y
                elif num == "-":
                    val = x-y
                elif num == "/":
                    if (x/y)<0:
                        val = int(ceil(x/y))
                    else:
                        val = int(x//y)
                else:
                    val = x*y
                stack.append(val)
            # print(stack)
        return stack.pop()