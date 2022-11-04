import io
import sys

_INPUT = """\
2 3 4
"""

sys.stdin = io.StringIO(_INPUT)



n,x,y = map(int,input().split())

from  functools import lru_cache

if n == 1:
    print(0)
    exit()

@lru_cache
def f(n,x,y,color):
    if n == 1 and color == "blue":
        return 1
    elif n == 1 and color == "red":
        return 0
    else:
        if color == "red":
            return f(n-1,x,y,"red")+ f(n,x,y,"blue") * x
        elif color == "blue":
            return f(n-1,x,y,"red")+ f(n-1,x,y,"blue") * y

print(f(n,x,y,"red"))