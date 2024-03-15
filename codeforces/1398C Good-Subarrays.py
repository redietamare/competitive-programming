from collections import defaultdict
test = int(input())
for i in range(test):
    n = int(input())
    arr = list(map(int,input()))
    ans = 0
    pre = 0
    count = defaultdict(int)
    count[0] = 1
    for i,x in enumerate(arr):
        pre += x
        diff = pre - i - 1
        if diff in count:
            ans += count[diff]
        count[diff] += 1
    print(ans)