import io
import sys

_INPUT = """\
1 0 1
2 1 2
1 0 1
"""

sys.stdin = io.StringIO(_INPUT)
c1,c2,c3 = map(int,input().split())
c4,c5,c6 = map(int,input().split())
c7,c8,c9 = map(int,input().split())
x,y,z = c1+c5+c9,c2+c6+c7,c3+c4+c8
if x==y==z:
    print("Yes")
else:
    print('No')