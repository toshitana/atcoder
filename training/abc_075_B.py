#%%
import io
import sys

_INPUT = """\
3 5
.....
.#.#.
.....
"""

#%%
sys.stdin = io.StringIO(_INPUT)
H,W = map(int,input().split())

li = []
for i in range(int(H)):
    s=list(input())
    li.append(s)

dx = [-1,0,1]
dy = [-1,0,1]

for i in range(H):
    for j in range(W):
        c = 0
        if li[i][j] == "#":
            continue
        for x in dx:
            for y in dy:
                if 0 <= i + x < H and 0 <= j + y < W and li[i + x][j + y] == "#":
                    c += 1
        
        li[i][j] = c 

for i in li:
    map1 = map(str, i)
    print("".join(map1))