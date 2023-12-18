class ATM:

    def __init__(self):
        self.atm=[0]*5
        self.wd=[0]*5
        self.hashmap={0:20,1:50,2:100,3:200,4:500}
        self.atmcopy=[]
    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.atm[i]+=banknotesCount[i]
    def withdraw(self, amount: int) -> List[int]:
        self.wd=[0]*5
        self.atmcopy=self.atm.copy()
        for i in range(4,-1,-1):
            rem=amount//self.hashmap[i]
            if self.atm[i]>=rem:
                amount-=rem*self.hashmap[i]
                self.wd[i]=rem
                self.atm[i]-=rem
            else:
                amount-=self.atm[i]*self.hashmap[i]
                self.wd[i]=self.atm[i]
                self.atm[i]=0
        if amount==0:
            return self.wd
        else:
            self.atm=self.atmcopy.copy()
            return [-1]       


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)