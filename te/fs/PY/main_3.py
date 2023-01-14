#!/bin/python3

import math
import os
import random
import re
import sys


def multiply(a, b, bound):
    # write your code here
    ab = a * b
    print(ab)

    return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # q = int(input())
    q = 3
    for _ in range(q):
        a, b, bound = list(map(int, input().split()))
        try:
            res = multiply(a, b, bound)
            fptr.write("%d\n" % res)
            print(f"res: {res}")
        except ValueError as e:
            fptr.write("%s\n" % e)
    fptr.close()
