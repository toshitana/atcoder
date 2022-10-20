import io
import sys

_INPUT = """\
7
1 2 3 2 1 999999999 1000000000
"""

sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = list(map(int,input().split()))


count = 1
pre = A[0]
state = 0

for i in A[1:]:
    if pre < i:
        if state ==0:
            state = 1
            pre = i
            continue
        elif state ==-1:
            count += 1
            state = 0
    if pre > i:
        if state ==0:
            state = -1
            pre = i
            continue
        elif state == 1:
            count += 1
            state = 0
    pre = i

print(count)