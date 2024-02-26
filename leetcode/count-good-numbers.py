class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        p=n//2
        if n == 1:
            return 5
    
        oddindxs = n//2
        
        if n%2==0:
            evenindxs = n//2 
        else:
            evenindxs = n//2 +1 
        
       
        def evenindex(e,p):
            if p == 1:
                return e
            elif p % 2 == 0:
                return evenindex((e*e)%mod,p//2)
            elif p % 2 ==1:
                return e*evenindex((e*e)%mod,p//2)
        return (evenindex(5,evenindxs)*evenindex(4,oddindxs))%mod
       
        # def oddindex(p):
        #     if p == 1:
        #         return 1
            
        
      
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
