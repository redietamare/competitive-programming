class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.person = persons
        self.time = times
        self.ans = []
        res = self.person[0]
        count = defaultdict(int)
        maxx = float("-inf")
        for i in range(len(self.person)):
            count[self.person[i]] += 1
            if count[self.person[i]]>=maxx:
                maxx = max(count[self.person[i]],maxx)
                res = self.person[i]
            self.ans.append(res)
    def q(self, t: int) -> int:
        val = bisect_left(self.time,t)
        print(val)
        if val>=len(self.time):
            return self.ans[-1]
        else:
            if self.time[val] == t:
                return self.ans[val]
            else:
                return self.ans[val-1]
       

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)