import io
import sys

_INPUT = """\
2 10
20 20
"""

sys.stdin = io.StringIO(_INPUT)

n,x = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
count = 0

for i in A[:-1]:
    if i <= x:
        x -=i
        count +=1
    else:
        break

if A[-1] ==x:
    count+=1


print(count)
