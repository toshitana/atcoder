import io
import sys

_INPUT = """\
1000000000000000000 100
"""

sys.stdin = io.StringIO(_INPUT)

import math

A,B = map(int,input().split())

cou = 0
a_min = float('inf')
while(True):
    a = B*cou + A /math.sqrt(cou + 1)
    cou += 1
    if a_min >a:
        a_min = a
    else:
        print(a_min)
        exit()