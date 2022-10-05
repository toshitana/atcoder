import io
import sys

_INPUT = """\
20 3
0 5 15
"""

sys.stdin = io.StringIO(_INPUT)
K,N = map(int,input().split())
li = list(map(int,input().split()))
l = []
for i in range(len(li)-1):
    l.append(li[i+1] - li[i])
l.append(K - li[-1] + li[0])
print(K - max(l))
