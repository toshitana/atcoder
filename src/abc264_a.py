import io
from operator import index
import sys

_INPUT = """\
3 4
"""

sys.stdin = io.StringIO(_INPUT)
r,c= map(int,input().split())

if r > 8:
  r = 15 - r

if c > 8:
  c = 15 - c

if min(r,c) % 2 ==1:
  print("black")
else:
  print("white")