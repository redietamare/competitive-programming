class Solution:
    def intervalIntersection(self, fl: List[List[int]], sl: List[List[int]]) -> List[List[int]]:
        p1 = p2 = 0
        ans = []
        while p1<len(fl) and p2<len(sl):
            sp = max(sl[p2][0],fl[p1][0])
            ep = min(sl[p2][1],fl[p1][1])
            if ep>=sp:
                ans.append([sp,ep])
            if fl[p1][1]>sl[p2][1]:
                p2+=1
            else:
                p1 += 1
        return(ans)