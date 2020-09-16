#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    l = []
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if i >0 and i< len(arr) and j > 0 and j <len(arr):
                
                s = list((arr[i][j],arr[i-1][j],arr[i-1][j-1],arr[i-1][j+1],arr[i+1][j],arr[i+1][j-1],arr[i+1][j+1]))
                l.append(s)
                
        print("")
    print(l)
    m = -900
    for i in l:
        m = max(m,sum(i))
    return m



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
