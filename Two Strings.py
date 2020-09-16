#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter 


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    # print(set(s1))
    # print(set(s2))
    # print(set(s1).intersection(set(s2)))
    # if len(set(s1).intersection(set(s2))) >0:
    #     return "YES"
    # else:
    #     return "NO"
     
    cnt1 = {}
    cnt2 ={}
    for i in s1:
        if i not in cnt1:
            cnt1[i]=1
        else:
            cnt1[i]+=1
    for i in s2:
        if i not in cnt2:
            cnt2[i]=1
        else:
            cnt2[i]+=1

    print(cnt1)
    print(cnt2)
    for i in cnt1:
        print(i)
        if i in cnt2:
            return "YES"
    return "NO"

    


    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
