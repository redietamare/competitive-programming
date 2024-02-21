class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while maxDoubles>0 and target>1:
            if target%2 == 1:
                target -= 1
                moves += 1
            target = target//2
            moves += 1
            maxDoubles -= 1
            # print(target,moves)
        if target>1:
            moves +=target-1
        return moves
            