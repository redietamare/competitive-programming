class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        minn=float("inf")
        unwanted=set()
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                unwanted.add(fronts[i])
        for i in range(len(fronts)):
            if (fronts[i] not in unwanted):
                minn = min(minn,fronts[i])
            if (backs[i] not in unwanted):
                minn = min(minn,backs[i])
        if minn==float("inf"):
            return 0
        else:
            return minn