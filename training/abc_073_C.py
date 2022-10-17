import io
import sys

_INPUT = """\
4
2
5
5
2
"""

sys.stdin = io.StringIO(_INPUT)
N = int(input())
li = set([])
for i in range(N):
    Ai = int(input())
    if Ai in li:
        li.discard(Ai)
    else:
        li.add(Ai)

print(len(li))