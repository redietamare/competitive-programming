class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = -1
        h = len(letters)
        if target >= letters[-1]:
            return letters[0]
        while l + 1<h:
            mid = (l+h)//2
            if letters[mid]>target:
                h = mid
            else:
                l = mid
        return letters[h]