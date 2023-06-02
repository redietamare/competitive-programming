N=int(input())
listt=[]
for i in range(N):
    grades=input().strip()
    listt.append(grades)
rounded=[]
for i in range(len(listt)):
        for j in range(1,6):
            if (int(listt[i])+j)%5==0:
                rounded.append(int(listt[i])+j)
for i in range(len(listt)): 
    if int(listt[i])>=38:
        if (rounded[i]-int(listt[i]))<3:
           listt[i]=rounded[i]
        else:
            listt[i]=int(listt[i])      
    print(listt[i])
