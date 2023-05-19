# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
N=int(input())
d=deque()
for i in range(N):
    command=input().split()
    if command[0]=='append':
        d.append(command[1])
    elif command[0]=='pop':
        d.pop()
    elif command[0]=='popleft':
        d.popleft()
    else:
        d.appendleft(command[1])
print(*d)
