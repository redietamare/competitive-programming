# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
arr=input().split()
arr=list(map(int,arr))
a=input().split()
a=set(map(int,a))
b=input().split()
b=set(map(int,b))
happiness=0
for i in arr:
    if i in a:
        happiness+=1
    elif i in b:
        happiness-=1
print(happiness)
