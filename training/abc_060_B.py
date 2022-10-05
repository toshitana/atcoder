import io
import sys

_INPUT = """\
40 98 58
"""

sys.stdin = io.StringIO(_INPUT)
A,B,C = map(int,input().split())

mod = A % B

tmp = 0
for i in range(B):
    if mod == C or tmp == C:
        print("YES")
        exit()
    tmp = mod * i
    while tmp >= B:
        tmp -= B
print("NO")