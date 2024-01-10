class Solution:
    def maxConsecutiveAnswers(self, answer: str, k: int) -> int:
        count = defaultdict(int)
        count = {"T":0,"F":0}
        l = 0
        maxcon = 1
        for r in range(len(answer)):
            count[answer[r]]+=1
           # print(count)
            while min(count.values())>k:
                count[answer[l]] -= 1
                l+=1
            maxcon = max(maxcon,r-l+1)
        return maxcon
        