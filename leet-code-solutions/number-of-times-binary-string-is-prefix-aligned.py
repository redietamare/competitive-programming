class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        string = [0]*n
        rz = n 
        r1 = 0
        l1 = 0
        lz = 0
        count = 0
        for i in range(len(flips)):
            string[flips[i] - 1] = 1
            if flips[i] - 1 > i:
                r1 += 1
                rz -= 1
            elif flips[i]-1 < i:
                l1 += 1
                lz -= 1
            else: 
                r1+=1
                rz-=1
            if string[i] == 1:
                l1+=1
                r1-=1
            else:
                lz+=1
                rz-=1
            if (l1 == i+1) and (rz == n-i-1):
                count += 1
        return count