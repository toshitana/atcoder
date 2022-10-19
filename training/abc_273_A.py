import io
import sys

_INPUT = """\
10
"""

sys.stdin = io.StringIO(_INPUT)
a=int(input())

b = 1
c=0
for i in range(a):
    b = b * (i+1)
print(b)