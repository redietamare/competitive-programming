class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def powerof2(n):
            if n<1:
                return False
            if n==1:
                return True
            return powerof2(n/2)
        return powerof2(n)
        