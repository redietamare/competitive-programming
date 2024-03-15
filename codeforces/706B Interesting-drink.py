from bisect import bisect_left,bisect_right
shopes = int(input())
arr = list(map(int,input().split()))
arr.sort()
q = int(input())
for i in range(q):
    coin = int(input())
    val = bisect_right(arr,coin)
    print(val)
# print(arr)kk