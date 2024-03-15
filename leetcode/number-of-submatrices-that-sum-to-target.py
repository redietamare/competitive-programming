class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        cols = len(matrix[0])
        rows = len(matrix)
        subsum = []
        for i in range(rows):
            arr = [0]*cols
            subsum.append(arr)
        for r in range(rows):
            for c in range(cols):
                top = subsum[r-1][c] if r>0 else 0
                left = subsum[r][c-1] if c>0 else 0
                topleft = subsum[r-1][c-1] if min(r,c)>0 else 0
                subsum[r][c] = matrix[r][c] + top + left - topleft
        ans = 0
        for r1 in range(rows):
            for r2 in range(r1,rows):
                count = defaultdict(int)
                count[0] = 1
                for c in range(cols):
                    presum = subsum[r2][c] - (subsum[r1-1][c] if r1>0 else 0)
                    diff = presum - target
                    ans += count[diff]
                    count[presum] += 1
        return ans
