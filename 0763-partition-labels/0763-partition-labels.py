class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex={}
        for i in range(len(s)):
            lastindex[s[i]]=i
        end=0
        summ=0
        ans=[]
        for i in range(len(s)):
            summ+=1
            end=max(end,lastindex[s[i]])
            if i==end:
                ans.append(summ)
                summ=0
        return(ans)

