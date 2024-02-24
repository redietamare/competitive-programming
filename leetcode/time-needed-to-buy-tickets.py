class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        i = 0
        n = len(tickets)
        while tickets[k]>0:
            if tickets[i%n]!=0:
                tickets[i%n]-=1
                res += 1
            i+=1
            
        return res