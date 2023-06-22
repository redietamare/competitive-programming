class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n>0:
            poww=self.myPow(x,n//2)
            power=poww*poww*(x**(n%2))
        else:
            power=1/self.myPow(x,-n)
        return power
            
                
     
        