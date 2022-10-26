import io
import sys

_INPUT = """\
1000000000000000000 1
"""

sys.stdin = io.StringIO(_INPUT)
N,K = map(int,input().split())


min = abs(N-K)
while True:
    tmp = abs(min-K)
    if min > tmp:
        min = tmp
    else:
        break

print(min)