import io
import sys

_INPUT = """\
7 4
"""

sys.stdin = io.StringIO(_INPUT)
a,b = map(int,input().split())

print("{:.3f}".format(b/a))