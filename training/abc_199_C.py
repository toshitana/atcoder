import io
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

n = int(input())
S= list(input())
Q=int(input())

for i in range(Q):
    t,a,b = map(int,input().split())
    if t == 1:
        S[a-1],S[b-1] = S[b-1],S[a-1]
    if t == 2:
        mae = S[:n]
        ato = S[n:]
        ato[len(ato):len(ato)]= mae
        S = ato
print("".join(S))