class Solution: 
    # select(self, arr, i):
        # code here 
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min=i
            for j in range(i+1,n):
                if arr[min]>arr[j]:
                    min=j
            if (min!=i):
                arr[min],arr[i]=arr[i],arr[min]
