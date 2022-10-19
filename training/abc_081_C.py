import io
import sys

_INPUT = """\
5 2
1 1 2 2 5
"""

sys.stdin = io.StringIO(_INPUT)

n,k = map(int,input().split())
A = list(map(int,input().split()))

from collections import Counter

A = Counter(A)
b = sorted(A.items(), key=lambda x:x[1])
total = 0
step = 0

for i in range(len(A)-k):
    total += b[i][1]
print(total)