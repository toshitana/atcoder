import io
from operator import index
import sys

_INPUT = """\

"""

sys.stdin = io.StringIO(_INPUT)
N,M = map(int,input().split())
a_list=[list(map(int,input().split()))	 for i in range(N)]
c_list=[list(map(int,input().split()))	 for i in range(M)]

for i in a_list:
    min_distance = 2 * (10**9)
    tmp = 0
    index_ = 0
    for j,v in enumerate(c_list):
        tmp = abs(i[0] - v[0]) + abs(i[1] - v[1])
        if tmp < min_distance:
            min_distance = tmp
            index_ = j + 1
    print(index_)
