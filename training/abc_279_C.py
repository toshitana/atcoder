import io
import sys

_INPUT = """\
8 7
#..#..#
.##.##.
#..#..#
.##.##.
#..#..#
.##.##.
#..#..#
.##.##.
....###
####...
....###
####...
....###
####...
....###
####...
"""

sys.stdin = io.StringIO(_INPUT)
from collections import Counter
H,W = map(int,input().split())

S=[list(input()) for i in range(H)]
T=[list(input()) for i in range(H)]

#print(S)
#print(T)

s_ = [list(x) for x in zip(*S)]
t_ = [list(x) for x in zip(*T)]

#print(s_)
#print(t_)

s = ["".join(x) for x in s_]
t = ["".join(x) for x in t_]

#print(s)
#print(t)

ss = Counter(s)
tt = Counter(t)

#print(ss)
#print(tt)

for i in ss:
    if ss[i] != tt[i]:
        print("No")
        exit()

print("Yes")