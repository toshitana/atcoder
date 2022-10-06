import io
from operator import index
import sys

_INPUT = """\
7 6
......
....#.
.#....
..#...
..#...
......
.#..#.
"""

sys.stdin = io.StringIO(_INPUT)
H,W = map(int,input().split())

li = []
col = []
for i in range(H):
    tmp = input()
    if "#" in tmp:
        li.append(list(tmp))
        for j,v in enumerate(list(tmp)):
            if v == "#":
                col.append(j)

tmp_1 = sorted(set(col))

for i in li:
    for j in tmp_1:
        print(i[j],end="")
    print()



