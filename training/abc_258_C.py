import io
import sys

_INPUT = """\
10 8
dsuccxulnl
2 4
2 7
1 2
2 7
1 1
1 2
1 3
2 5
"""

sys.stdin = io.StringIO(_INPUT)
'''
from collections import deque
N,Q = map(int,input().split())
S = list(input())
S = deque(S)
for i in range(Q):
    t,x = map(int,input().split())
    if t == 1:
        for j in range(x):
            tmp = S.pop()
            S.appendleft(tmp)
    if t == 2:
        print(S[x-1])
'''
n, q = map(int, input().split())
s = input()
idx = 0
for _ in range(q):
    a, b = map(int, input().split())
    if a == 1:
        idx -= b
    else:
        print(s[(idx+b-1)%n])