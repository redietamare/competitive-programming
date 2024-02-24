class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = 0
        ones = 0
        zeroones =0
        onezeros = 0
        res  = 0
        for i in s:
            if i == "0":
                zeros += 1
                res += zeroones
                onezeros += ones
            if i == "1":
                ones += 1
                res += onezeros
                zeroones += zeros
        return res