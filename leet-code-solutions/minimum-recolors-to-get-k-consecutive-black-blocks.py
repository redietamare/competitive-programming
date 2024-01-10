class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = blocks[:k-1].count("W")
        minops = float("inf")
        for i in range(len(blocks)-k+1):
            if blocks[i+k-1] == "W":
                whites += 1
            minops = min(minops,whites)
            if blocks[i] =="W":
                whites-=1
        return minops