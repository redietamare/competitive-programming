# Enter your code here. Read input from STDIN. Print output to STDOUT
N,X=map(int,input().split())
listt=[]
for i in range(X):
    x=list(map(float,(input().split())))
    listt.append(x)
#print(listt)
zipp=list(zip(*listt))
#print(zipp)
for i in zipp:
    sum=0
    for j in i:
        sum+=j
    av=sum/X
    print(av)
