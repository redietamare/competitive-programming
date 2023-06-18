class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        words.reverse()
        reverse=" ".join(words)
        return(reverse)