import io
from operator import index
import sys
from turtle import distance

_INPUT = """\
2
5 1 1
100 1 1
"""

sys.stdin = io.StringIO(_INPUT)
N = int(input())
a_list=[list(map(int,input().split()))	for i in range(N)]


now = [0,0,0]
distance = 0
for i in a_list:
    distance = abs(now[1] - i[1]) + abs(now[2]- i[2])
    t = i[0] - now[0]
    if distance > t:
        print("No")
        exit()
    elif (distance - t) % 2 == 1:
        print("No")
        exit()
    else:
        now = i
print("Yes")