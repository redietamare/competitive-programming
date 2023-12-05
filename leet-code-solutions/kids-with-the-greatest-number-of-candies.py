class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxnum = max(candies)
        ans=[]
        for candy in candies:
            
            if candy+extraCandies>=maxnum:
                ans.append(True)
            else:
                ans.append(False)
        return ans
            