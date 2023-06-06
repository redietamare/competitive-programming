n=int(input())
arr=list(map(int,input().split()))
counter=[]
x=max(arr)
for i in range(100):
    counter.append(0)
for i in range(len(arr)):
    counter[arr[i]]+=1
print(*counter)
