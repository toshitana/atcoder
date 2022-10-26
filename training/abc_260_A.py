import io
from operator import index
import sys

_INPUT = """\
a
"""

sys.stdin = io.StringIO(_INPUT)


import sys
input=lambda :sys.stdin.readline()[:-1]
def MI(): return map(int, input().split())

s = input()
from collections import Counter
cnt = Counter(list(s))
for key, value in cnt.items():
    if value==1:
        print(key); exit()
print(-1)