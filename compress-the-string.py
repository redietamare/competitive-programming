# Enter your code here. Read input from STDIN. Print output to STDOUT
S=input()
S=list(S)
print(S)
listt=[]
for i in S:
    i=int(i)
    listt.append(i)
print(listt)
for i in range(len(listt)):
    listt[i]=str(listt.count(listt[i]))+ str(listt[i])
print(listt)
