import io
import sys

_INPUT = """\
3
5
10
15
"""

sys.stdin = io.StringIO(_INPUT)

from collections import deque
n=int(input())
li = list(map(int,input().split()))