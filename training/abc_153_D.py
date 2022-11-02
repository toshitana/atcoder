import io
import sys

_INPUT = """\
1000000000000
"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
from  functools import lru_cache

@lru_cache
def f(x):
    if x == 1:
        return 1
    else:
        return  f(x//2) * 2 + 1

print(f(N))