import io
import sys

_INPUT = """\
4 2
3 1 2 4
3 2 3 4
"""

sys.stdin = io.StringIO(_INPUT)

from itertools import combinations

N,M = map(int,input().split())

int_list=[list(map(int,input().split())) for i in range(M)]

l2d = [[0] * N for i in range(N)]
for i,v in enumerate(int_list):
    tmp_li = v[1:]
    p = combinations(tmp_li,2)
    for j in p:
        l2d[j[0]-1][j[1]-1] = 1
        l2d[j[1]-1][j[0]-1] = 1

for i in l2d:
    if sum(i) < N-1:
        print("No")
        exit()
    else:
        continue
print("Yes")
