# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A=input().split()
A=set(map(int,A))
B=input().split()
B=set(map(int,B))
productt=(list(product(A,B)))
print(*productt)
