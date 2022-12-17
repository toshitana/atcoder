import io
from operator import index
import sys

_INPUT = """\
9
"""

sys.stdin = io.StringIO(_INPUT)

a=int(input())

for i in range(a,-1):
    print(i)