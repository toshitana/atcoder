import io
import sys

_INPUT = """\
5
31 41 59 26 53
"""

sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = list(map(int,input().split()))

A = sorted(A)

S = [0]
sum = 0
for i in A:
    sum += i
    S.append(sum)

ans = 0
for i,ai in enumerate(A):
    ans += ai * (i+1) - S[i+1]

print(ans)