if __name__ == '__main__':
    n = int(input())
    arr=input().split()
    arr=list(map(int,arr))    
    t=tuple(arr)
    x=hash(t)
    print(x)
