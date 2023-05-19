from collections import OrderedDict
N=int(input())
ordereddict=OrderedDict()
for i in range(N):
    x=input().split()
    name=" ".join(x[0:-1])
    if name in ordereddict:
        ordereddict[name]+=int(x[-1])
    else:
        ordereddict[name]=int(x[-1])
    #print(name)
    #print(x[-1])
#print(ordereddict)
for i in ordereddict:
    print(i,ordereddict[i])
