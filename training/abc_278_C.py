import io
import sys

_INPUT = """\
10 30
3 1 6
3 5 4
1 6 1
3 1 7
3 8 4
1 1 6
2 4 3
1 6 5
1 5 6
1 1 8
1 8 1
2 3 10
1 7 6
3 5 6
1 6 7
3 6 7
1 9 5
3 8 6
3 3 8
2 6 9
1 7 1
3 10 8
2 9 2
1 10 9
2 6 10
2 6 8
3 1 6
3 1 8
2 8 5
1 9 10
"""

sys.stdin = io.StringIO(_INPUT)

N,Q = map(int,input().split())

li = [[0] * (N+10) for i in range(N+10)]

for i in range(Q):
    t,a,b = map(int,input().split())
    if t == 1:
        li[a-1][b-1] = 1
    if t == 2:
        li[a-1][b-1] = 0
    if t == 3:
        if li[a-1][b-1] == 1 and li[b-1][a-1] == 1:
            print("Yes")
        else:
            print("No")