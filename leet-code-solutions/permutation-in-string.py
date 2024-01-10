class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cs1 = Counter(s1)
        ls1 = len(s1)
        cs2 = Counter(s2[:ls1-1])
        for i in range(len(s2)-ls1+1):
            cs2[s2[i+ls1-1]]+=1
            if cs2 == cs1:
                return True
            cs2[s2[i]]-=1
        return False
    