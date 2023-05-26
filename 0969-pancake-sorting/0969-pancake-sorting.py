class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n=len(arr)
        ans=[]
        for i in range(n):
            maximum=max(arr[0:n-i])
            maxindex=arr[0:n-i].index(maximum)
            k=maxindex+1
            arr[0:k]=arr[0:k][::-1]
            ans.append(k)
            arr[0:n-i]=arr[0:n-i][::-1]
            ans.append(n-i)
        return(ans)