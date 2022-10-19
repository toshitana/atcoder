import io
import sys

_INPUT = """\
2
1 0
"""

sys.stdin = io.StringIO(_INPUT)
n = input()
A = list(map(int,input().split()))

A = sorted(A,reverse=True)

max2_even = []
max2_odd = []

for i in A:
    if i % 2 == 0:
        max2_even.append(i)
    else:
        max2_odd.append(i)
    if len(max2_even) >= 2 or len(max2_odd) >= 2:
        print(max(sum(max2_even),sum(max2_odd)))
        exit()
print(-1)