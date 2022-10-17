import io
import sys

_INPUT = """\
100000 5
"""

sys.stdin = io.StringIO(_INPUT)
N,K = map(int,input().split())

P = 0
for i in range(1,N + 1):
    tmp = i
    count = 0
    while(tmp < K):
        tmp *=2
        count +=1

    P += (0.5**count)*(1/N)
print(P)