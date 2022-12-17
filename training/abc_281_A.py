import io
from operator import index
import sys

_INPUT = """\
3
"""

sys.stdin = io.StringIO(_INPUT)

a=int(input())

for i in reversed(range(a+1)):
    print(i)