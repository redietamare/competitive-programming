class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        def power(x,n):
            if n == 1:
                return x
            elif n%2==0:
                return power(x*x,n//2)
            elif n%2==1:
                return x*power(x*x,n//2)
        if n < 0:
            ans =  power(x,abs(n))
            return 1/ans
        else:
            return power(x,n)
            