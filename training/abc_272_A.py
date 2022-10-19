import io
import sys

_INPUT = """\
3
2 7 2
"""

sys.stdin = io.StringIO(_INPUT)
n = input()
li = list(map(int,input().split()))
print(sum(li))