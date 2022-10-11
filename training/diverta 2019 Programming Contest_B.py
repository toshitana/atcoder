import io
import sys
import math
_INPUT = """\
13 1 4 3000
"""
sys.stdin = io.StringIO(_INPUT)

import math
R,G,B,N = map(int,input().split())

sum_ = 0
for r in range(math.floor(N/R)+1):
    for g in range(math.floor(N/G)+1):
        b = N - r*R - g*G
        if b % B == 0 and b >= 0:
            sum_ += 1
            #print(r,g,int(b/B))

print(sum_)
