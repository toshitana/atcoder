import io
import sys

_INPUT = """\
10
314159265 358979323 846264338 -327950288 419716939 -937510582 97494459 230781640 628620899 -862803482
"""

sys.stdin = io.StringIO(_INPUT)

n = input()
li = list(map(int,input().split()))

li1 = []
for i,v in enumerate(li):
    if i == 0:
        li1.append(v)
    else:
        li1.append(v-li[i-1])

map1 = map(str, li1)
print(" ".join(map1))