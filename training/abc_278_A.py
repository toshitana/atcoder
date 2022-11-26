import io
import sys

_INPUT = """\
3 2
2 7 8
"""

sys.stdin = io.StringIO(_INPUT)


from collections import deque
x,y = map(int,input().split())
li = list(map(int,input().split()))

d = deque(li)

for i in range(y):
	d.popleft()
	d.append(0)

print(' '.join(map(str, d)))
# %%
