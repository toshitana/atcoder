import io
import sys

_INPUT = """\
1
99999
"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
li = list(map(int,input().split()))
lis = [0] * (10**5+2)
for i in li:
    lis[i-1] += 1
    lis[i] += 1
    lis[i+1] += 1

print(max(lis))