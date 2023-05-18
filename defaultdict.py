from collections import defaultdict
n,m=(input()).split()
n,m=map(int,(n,m))
A=defaultdict(list)
B=[]
for i in range(n):
    A[input()].append(i+1)
for i in range(m):
    B.append(input())
for i in B:
    if i in A:
        print(*(A[i])) 
    else:
        print(-1)
