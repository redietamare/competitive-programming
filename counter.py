# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
N=int(input())
list1=list(map(int,input().split()))
c=int(input())
dic=Counter(list1)

total=0
for i in range(c):
    a,b=(list(map(int,input().split())))
    if dic[a]>0:
        total+=b
        dic[a]-=1
print(total)
        
