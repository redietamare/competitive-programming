class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ans = ''
        prefix = [0]*len(s)
        for shift in shifts:
            l = shift[0]
            r = shift[1]
            k = shift[2]
            if k == 0:
                prefix[l] -= 1
                if r+1<len(s):
                    prefix[r+1] += 1
            else:
                prefix[l] += 1
                if r+1<len(s):
                    prefix[r+1] -=1
        mainpre = []
        runsum =0
        for i in prefix:
            runsum+=i
            mainpre.append(runsum)
        for i in range(len(mainpre)):
            if (ord(s[i])+(mainpre[i])%26)>122:
                ans += chr((ord(s[i])+(mainpre[i])%26)-26)
            else:
                ans += chr(ord(s[i])+(mainpre[i])%26)
        return ans
        
#         ans =''
#         prefix = [0]*len(s)
#         for shift in shifts:
#             start = shift[0]
#             end = shift[1]
#             if shift[2] == 0 :
#                 forb=-1
#             else:
#                 forb=1
#             for i in range(start,end+1):
#                 prefix[i]+=forb
#         # print(prefix)
        # for i in range(len(prefix)):
        #     if (ord(s[i])+(prefix[i])%26)>122:
        #         ans += chr((ord(s[i])+(prefix[i])%26)-26)
        #     else:
        #         ans += chr(ord(s[i])+(prefix[i])%26)
        # return ans
                