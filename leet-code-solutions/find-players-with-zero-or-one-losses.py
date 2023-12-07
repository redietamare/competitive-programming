class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = []
        winner = []
        loser = []
        winans=set()
        for match in matches:
            winner.append(match[0])
            loser.append(match[1])
        loserset=set(loser)
        for i in winner:
            if i not in loserset:
                winans.add(i)
        loserans=[]
        losercount=Counter(loser)
        for i in losercount:
            if losercount[i]==1:
                loserans.append(i)
        winans=list(winans)
        winans.sort()
        loserans.sort()
        ans=[winans,loserans]
        return ans
            