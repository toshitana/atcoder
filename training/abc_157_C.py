import io
import sys

_INPUT = """\
3 2
2 1
2 3
"""

sys.stdin = io.StringIO(_INPUT)
N,M = map(int,input().split())


ans = [0] * N


for i in range(M):
    s,c = map(int,input().split())
    if ans[s - 1] != 0 and ans[s - 1] != c:
        print("-1")
        exit()
    elif s == 1 and c == 0:
        if N > 1:
            print("-1")
            exit()
    ans[s - 1] = c

if N > 1 and ans[0] == 0:
    ans[0] = 1

map1 = map(str, ans)
print("".join(map1)) 