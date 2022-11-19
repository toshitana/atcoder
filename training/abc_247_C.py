import io
import sys

_INPUT = """\
4
"""

sys.stdin = io.StringIO(_INPUT)
N = str(input())
from  functools import lru_cache

@lru_cache
def S(x):
    if x == "1":
        return "1"
    
    return str(S(str(int(x)-1))) + " " + x + " " + str(S(str(int(x)-1)))

print(S(N))