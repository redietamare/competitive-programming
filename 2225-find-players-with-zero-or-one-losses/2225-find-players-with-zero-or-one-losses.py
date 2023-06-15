class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners=set()
        losers=[]
        ans1=[]
        ans2=[]
        ans=[]
        for i in range(len(matches)):
            winners.add(matches[i][0])
            losers.append((matches[i][1]))
        counter=Counter(losers)
        losers=set(losers)
        for winner in winners:
            if winner not in losers:
                ans1.append(winner)
        for i in counter:
            if counter[i]==1:
                ans2.append(i)
        ans1.sort()
        ans2.sort()
        ans.append(ans1)
        ans.append(ans2)
        return(ans)
        
                
                
        