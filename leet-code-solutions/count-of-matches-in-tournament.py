class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        teams = n
        while teams!=1:
            matches += teams//2
            if teams % 2 != 0:
                teams = (teams//2) + 1
            else:
                teams = teams//2
        return(matches)