# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
S,k=input().split()
Slist=list(S)
Slist.sort()
listt=(list(permutations(Slist,int(k))))
for i in listt:
    print("".join(i))
