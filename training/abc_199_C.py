import io
from re import L
import sys

_INPUT = """\
2
FLIP
6
1 1 3
2 0 0
1 1 2
1 2 3
2 0 0
1 1 4
"""

sys.stdin = io.StringIO(_INPUT)

def change(a,b,L):
    ai = 0
    bi = 0
    if a > n:
        a = a - n
        ai = 1
    if b > n:
        b = b -n
        bi = 1
    #print(L,a,b)
    L[ai][a-1],L[bi][b-1] = L[bi][b-1],L[ai][a-1]
    return L



n = int(input())
S= list(input())
Q=int(input())

_first = list(S[:n])
_second = list(S[n:])
L = [_first, _second]

for i in range(Q):
    t,a,b = map(int,input().split())
    if t == 1:
        L = change(a,b,L)
    if t == 2:

        L[0],L[1] = L[1],L[0]
print("".join(L[0])+"".join(L[1]))