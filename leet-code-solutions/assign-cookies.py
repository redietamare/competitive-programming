class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        pg = 0
        ps = 0
        content = 0
        while pg < len(g) and ps <len(s):
            if g[pg] <= s[ps]:
                content += 1
                pg += 1
            ps += 1
        return content