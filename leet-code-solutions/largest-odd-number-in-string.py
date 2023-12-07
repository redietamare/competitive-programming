class Solution:
    def largestOddNumber(self, num: str) -> str:
        maxodd=""
        for i in range(len(num)):
            if int(num[i])%2!=0:
                maxodd=num[:i+1]
        return maxodd
        
        
        
        
        
        
        
        
        
        
        
        # maxodd=0
        # for i in range(len(num)):
        #     for j in range(i,len(num)):
        #         number=int(num[i:j+1])
        #         if number%2!=0:
        #             maxodd=max(maxodd,number)
        # if maxodd==0:
        #     return ""
        # else:
        #     return str(maxodd)
                