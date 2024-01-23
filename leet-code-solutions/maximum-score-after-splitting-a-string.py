class Solution:
    def maxScore(self, s: str) -> int:


        s = list(map(int,s))
        lz = s[:1].count(0)
        lo = s[:1].count(1)
        rz = s[1:].count(0)
        ro = s[1:].count(1)
        maxsum = lz + ro
        for i in range(1,len(s)-1):
            if s[i] == 0:
                lz += 1
                rz -= 1
            else:
                lo += 1
                ro -= 1
            maxsum = max(maxsum,lz+ro)
        return maxsum
        