class Solution:
    def arraySortedOrNot(self, arr, n):
        for i in range(len(arr)-1):
            if not arr[i]<=arr[i+1]:
                return 0
        return 1
                
