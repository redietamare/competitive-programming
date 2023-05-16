# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 
AB=int(input())
BC=int(input())
x=math.atan(BC/AB)
deg=math.degrees(x)
a=90-deg
a=round(a)
a=str(a)
print(a+chr(176))
