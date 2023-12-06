class Solution:
    def totalMoney(self, n: int) -> int:
        num=1
        tempnum=0
        summ=0
        for i in range(n):
            
            if i%7 == 0:
                num = 1 + tempnum
                tempnum += 1
                
            summ +=  num
            num += 1
            
            
        return summ