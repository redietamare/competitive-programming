class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2!=1:
            return n
        else:
            return n+n