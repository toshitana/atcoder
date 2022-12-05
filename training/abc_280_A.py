import io
import sys

_INPUT = """\
3 5
#....
.....
.##..
"""

sys.stdin = io.StringIO(_INPUT)

H,W = map(int,input().split())

S=[list(input()) for i in range(H)]

sum_ = 0
for i in S:
    sum_ += i.count("#")

print(sum_)