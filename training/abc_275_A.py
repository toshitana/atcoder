import io
import sys

_INPUT = """\
10
22 75 26 45 72 81 47 29 97 2
"""

sys.stdin = io.StringIO(_INPUT)

n = int(input())

li = list(map(int,input().split()))
print(li.index(max(li))+1)