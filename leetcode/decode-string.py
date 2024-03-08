class Solution:
    def decodeString(self, s: str) -> str:        
        
        
        
        
        
#         stack=[]
#         for i in range(len(stack)):
#             if i !=']':
#                 stack.append(s[i])
#             else:
#                 string=""
#                 while stack[-1]!="[":
#                     string=stack.pop() + string
#                 stack.pop()
#                 k=""
#                 while stack and stack[-1].isdigit():
#                     k=stack.pop() + k        stack = []
#                 stack.append(int(k)*string)
#         return "".join(stack)
        stack=[]
        for c in s:
            if c != "]":
                stack.append(c)
            else:
    
                sub_string = ""
                while stack and stack[-1] != "[":
                    sub_string += stack.pop()
                stack.pop()
               
                number = ""
                while stack and stack[-1].isdigit():
                    number += stack.pop()
               
                number = number[::-1]
               
                stack.append(int(number) * sub_string)

        return ''.join([sub_string[::-1] for sub_string in stack])

        
        
        
        
        
#         dstack=[]
#         cstack=[]
#         bstack=[]
#         ccount=""
#         res=""
#         st=""
#         for i in s:
#             if not i.isalnum():
#                 if ccount:
#                     cstack.append(ccount)
#                     ccount=''

#             if i.isdigit():
#                 dstack.append(int(i))
#             if i.isalpha():
#                 ccount+=i
#             if i=="[":
#                 bstack.append(i)
#             print(cstack,dstack,bstack,ccount)
#             if i=="]":
#                 st=st+cstack[-1]
#                 st=dstack[-1]*st
#                 # res=res+cstack[-1]
#                 # res=dstack[-1]*res
#                 dstack.pop()
#                 cstack.pop()
#                 bstack.pop()
#                 if cstack:
#                     st=cstack[-1]+st
#                 res+=st
#                 st=''
#             print(res)
#         return res
                
            