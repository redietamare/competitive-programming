class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)
        left=0
        right=len(skill)-1
        ans=[]
        summ=[]
        prod=1
        summm=0
        skill.sort()
        while left<n/2 and n/2<=right:
            ans.append((skill[left],skill[right]))
            summ.append(skill[left]+skill[right])
            left+=1
            right-=1
        if len(set(summ))==1:
            for i in ans:
                prod=i[0]*i[1]
                summm+=prod
            return(summm)
        else:
            return -1
