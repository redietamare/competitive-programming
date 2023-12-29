class Solution:
    def smallestNumber(self, num: int) -> int:
        numstr = list(str(num))
        zeros = numstr.count("0")
        if num==0:
            return 0
        if num<0:
            numstr.remove("-")
        for i in range(len(numstr)):
            numstr[i]=int(numstr[i])
        newarr = []
        ans = ""
        for i in range(len(numstr)):
            if numstr[i] != 0:
                newarr.append(numstr[i])
        newarr.sort()

        if num>0:
            number = str(newarr[0])
            number += "0"*zeros
            for i in range(1,len(newarr)):
                number += str(newarr[i])
            return int(number)
        else:
            number=str(newarr[-1])
            for i in range(len(newarr)-2,-1,-1):
                number += str(newarr[i])
            number += "0"*zeros
            return int("-"+ number)
            