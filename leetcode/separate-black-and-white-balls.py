class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = s.count("1")
        swaps = 0
        left = 0
        right = len(s)-1
        while left<right:
            # print(s[left],s[right])
            if s[left]=="1" and s[right]=="0":
                swaps += right - left
                left+=1
                right-=1
            elif s[left] == "1" and s[right]=="1":
                right-=1
            else:
                left+=1
        return swaps
                
                
            