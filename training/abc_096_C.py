import io
import sys


_INPUT = """\
11 11
...#####...
.##.....##.
#..##.##..#
#..##.##..#
#.........#
#...###...#
.#########.
.#.#.#.#.#.
##.#.#.#.##
..##.#.##..
.##..#..##.
"""

sys.stdin = io.StringIO(_INPUT)
H,W = map(int,input().split())
li=[list(input()) for k in range(H)]

for i in range(H):
    for j in range(W):
        if li[i][j] == "#":
            if 0 <= i - 1 and li[i-1][j] == "#":
                continue
            elif 0 <= j - 1 and li[i][j-1] == "#":
                continue
            elif i + 1 < H and li[i+1][j] == "#":
                continue
            elif j - 1 < W and li[i][j+1] == "#":
                continue
            else:
                print("No")
                exit()

print("Yes")