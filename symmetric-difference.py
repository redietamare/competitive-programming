M=int(input())
a=input().split()
a=set(map(int,a))
N=int(input())
b=input().split()
b=set(map(int,b))
ans=[]
for i in a :
    if i not in b:
        ans.append(i)
for j in b:
    if j not in a:
        ans.append(j)
ans.sort()
for i in ans:
    print(i)
            
