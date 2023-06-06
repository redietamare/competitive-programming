#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    last=arr[-1]
    index=0

    for i in range(2,len(arr)+2):
        if last<arr[(n-i)]:
            if (n-i)>=0:
                arr[n-i+1]=arr[n-i]
                print(*arr)
            else:
                arr[n-i+1]=last
                print(*arr)
                break
        else:
            arr[n-i+1]=last
            print(*arr)
            break
  

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
