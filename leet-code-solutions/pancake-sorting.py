class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        for i in range(len(arr)):
            maxel = max(arr[:len(arr)-i])
            ind = arr[:len(arr)-i].index(maxel)
            arr[:ind+1] = arr[:ind+1][::-1]
            flips.append(ind+1)
            arr[:len(arr)-i] = arr[:len(arr)-i][::-1]
            flips.append(len(arr)-i)
        return flips