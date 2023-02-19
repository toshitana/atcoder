import io
import sys

_INPUT = """\
3 8
1 2 3 4 4 4 4 4 4 4
"""

sys.stdin = io.StringIO(_INPUT)


N, K = map(int, input().split())
A = list(map(int, input().split()))

import sys
A.sort()
A = list(set(A))

if len(A) < K:
    for index, a in enumerate(A):
        if index != a:
            print(index)
            sys.exit()

B = A[:K]

i = 0
for a in B:
    if a == i:
        i += 1

print(i)
