# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
S,k=input().split()
s=list(S)
s.sort()
listt=[]
for i in range(1,int(k)+1):
    x=list(combinations(s,i))
    listt.append(x)
for i in listt:
    for x in i:
        print("".join(x))
