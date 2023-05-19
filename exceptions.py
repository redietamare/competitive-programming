# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
for i in range(N):
    a,b=input().split()
    try:
        a=int(a)
        b=int(b)
        x=a/b
        print(int(x))
    except ZeroDivisionError :
        print (("Error Code:"),"integer division or modulo by zero")
    except ValueError as f:
        print (("Error Code:"),f)
