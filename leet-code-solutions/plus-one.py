class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i]=str(digits[i])
        num=int("".join(digits))
        num+=1
        nums=str(num)
        ans=[]
   
        for i in range(len(nums)):
            mod=num%10
            
            num//=10
            ans.append(mod)
        return ans[::-1]