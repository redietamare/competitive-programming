class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0
        n = len(cardPoints)
        summ = sum(cardPoints)
        winsize = n-k
        if k==n:
            return summ
        else:
            wind_sum = sum(cardPoints[:(winsize-1)])
            
        maxsum = 0
        
        for i in range(n-winsize+1):
            wind_sum += cardPoints[i+winsize-1]
            out_wind_sum = summ - wind_sum
            maxsum = max(maxsum,out_wind_sum)
            wind_sum -= cardPoints[i]
        return maxsum
            