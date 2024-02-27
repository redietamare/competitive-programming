class Solution:
    def bestClosingTime(self, customers: str) -> int:
        leftNo = 0
        rightYes = customers.count("Y")
        minn =  float("inf")
       
        for i in range(len(customers)):
            if minn > leftNo + rightYes:
                minn = min (minn,leftNo + rightYes)
                ind  = i
            if customers[i] =="N":
                leftNo += 1
            else:
                rightYes -=1
            
        if minn > leftNo:
            minn = leftNo
            ind = len(customers)
        return ind