import io
import sys

_INPUT = """\
4
1 3 5 2
"""

sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = list(map(int,input().split()))

li = [0] * (2*n + 1)

for i,v in enumerate(A):
    tmp = li[v-1]
    li[2*i+1] = tmp +1
    li[2*i+2] = tmp +1

for i in li:
    print(i)