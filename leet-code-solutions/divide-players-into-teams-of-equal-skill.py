class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        equal = skill[0]+skill[len(skill)-1]
        l = 0
        r = len(skill)-1
        chem = 0
        while l<r:
            if skill[l]+skill[r]!=equal:
                return -1
            else:
                chem += skill[l]*skill[r]
            r-=1
            l+=1
        return chem