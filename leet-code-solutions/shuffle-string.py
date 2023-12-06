class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [""]*(len(s))
        p1 = 0
        while p1 < len(s):
            ans[indices[p1]] = s[p1]
            p1+=1
        return "".join(ans)