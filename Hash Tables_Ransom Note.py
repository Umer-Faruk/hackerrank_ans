#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # print(magazine)
    # print(note)
    c1 = {}
    c2 = {}
    for i in magazine:
        if i not in c1:
            c1[i] = 1
        else:
            c1[i] +=1
    for j in note:
        if j not in c2:
            c2[j] = 1
        else:
            c2[j] +=1

   
    for i in c2.keys():
        # print(c2[i] == c1[i])
        try:
            if c2[i] <= c1[i]:
            # print(c1[i])
                continue
            else:
                return "No"
        except:
            return"No"

    return "Yes"


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
