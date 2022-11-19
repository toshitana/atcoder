import io
import sys

_INPUT = """\
0
"""

sys.stdin = io.StringIO(_INPUT)
import math
def f(x,li):
    if li[math.floor(x/2)] != 0 and li[math.floor(x/3)] !=0:
        #print(1)
        li[x] = li[math.floor(x/2)] + li[math.floor(x/3)]
        return li[math.floor(x/2)] + li[math.floor(x/3)]
    elif li[math.floor(x/2)] == 0 and li[math.floor(x/3)] !=0:
        #print(2)
        tmp = f(math.floor(x/2),li)
        li[x] = tmp + li[math.floor(x/3)]
        return tmp + li[math.floor(x/3)]
    else:
        tmp1 = f(math.floor(x/2),li)
        tmp2 = f(math.floor(x/3),li)
        li[x] = tmp1 + tmp2
        return tmp1 + tmp2

n = int(input())


if n == 0:
    print(1)
    exit()
else:
    li = [0] * (n + 1)
    li[0] = 1

print(f(n,li))