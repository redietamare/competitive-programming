n = int(input())
people = list(map(int,input().split()))
speed = list(map(int,input().split()))
def checker(t):
    maxdis_fromright = float("-inf")
    for i in range(len(people)):
        dis = speed[i]*t
        maxdis_fromright = max(maxdis_fromright ,people[i]-dis)
    mindis_fromleft = float("inf")
    for i in range(len(people)):
        dis = speed[i]*t
        mindis_fromleft = min(mindis_fromleft,people[i]+dis)
    if  mindis_fromleft >=  maxdis_fromright:
        return True
    else:
        return False
def helper():
    l = 0.0
    r = 10**9
    while abs(r-l)>=10**(-6):
        time = (l+r)/2
        if checker(time):
            r = time
            ans = time
        else:
            l = time 
    return ans
print(helper())