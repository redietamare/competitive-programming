class Solution:
    def isHappy(self, n: int) -> bool:
        sett=set()
        summ=0
        nn=len(str(n))
        for i in range(nn):
            summ+=((int(str(n)[i]))**2)
        while(summ not in sett):
            sett.add(summ)
            s=0
            while(summ)!=0:
                mod=summ%10
                mod=mod**2
                s+=mod
                summ//=10
            summ=s
            if summ==1:
                return True
        return False
                
        