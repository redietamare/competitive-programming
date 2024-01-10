class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a","e","i","o","u"}
        vow = 0
        maxvows = 0
        for i in range(len(s[:k-1])):
            if s[i] in vowels:
                vow+=1
        for i in range(len(s)-k+1):
            if s[i+k-1] in vowels:
                vow += 1
            maxvows = max(maxvows,vow)
            if s[i] in vowels:
                vow -= 1
        return maxvows