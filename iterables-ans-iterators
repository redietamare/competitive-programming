# Enter your code here. Read input from STDIN. Print output to STDOUTdf
from itertools import combinations
n=int(input())
N=input().split()
list1=list(N)
K=int(input())
#print(list1)
list2=[]
for i in range(len(list1)):
    y=(i+1)
    list2.append(y)
#print(list2)
list3= list(combinations(list2,K))
#print(list3)
list4=[]
for i in range(len(list1)):
    if list1[i]=="a":
        x=i+1
        list4.append(x)      
#print(list4)
count=0
for i in list3:
    if len(i)+ len(list4)!=len(set(list4+list(i))):
        count+=1
z=count/len(list3)
a=format(z,'.3f') 
print(a)  
