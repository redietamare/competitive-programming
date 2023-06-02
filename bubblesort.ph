#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    count=0
    for i in range(len(a)):
        for j in range(len(a)-1):
    
            if a[j]>a[j+1]:
             r=a[j]
             a[j]=a[j+1]
             a[j+1]=r
             count+=1
    f=a[0]
    l=a[-1]
    print("Array is sorted in " + str(count) + " swaps.")
    print("First Element: " + str(f))
    print("Last Element: " + str(l))
       
             
        
            
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    
    countSwaps(a)
