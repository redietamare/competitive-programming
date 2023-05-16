if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sett=list(set(arr))
    sett.sort()
    print(sett[-2])
