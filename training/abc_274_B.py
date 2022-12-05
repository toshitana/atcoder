import io
import sys

_INPUT = """\
5 47
.#..#..#####..#...#..#####..#...#...###...#####
.#.#...#.......#.#...#......##..#..#...#..#....
.##....#####....#....#####..#.#.#..#......#####
.#.#...#........#....#......#..##..#...#..#....
.#..#..#####....#....#####..#...#...###...#####
"""

sys.stdin = io.StringIO(_INPUT)

from collections import Counter
H,W = map(int,input().split())

sum = [0] * W
for i in range(H):
    s=list(input())
    for j,v in enumerate(s):
        if v == "#":
            sum[j] += 1

for i in sum:
    print(i)