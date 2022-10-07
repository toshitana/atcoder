import io
from operator import index
import sys

_INPUT = """\
3
5
10
15
"""

sys.stdin = io.StringIO(_INPUT)
n=int(input())

int_list = []
no_zero_list = []

for i in range(n):
    s = int(input())
    int_list.append(s)
    if s % 10 != 0:
        no_zero_list.append(s)


sum_ = sum(int_list)
int_list.sort()

if sum_ % 10 !=0:
    print(sum_)
    exit()
else:
    if len(no_zero_list) > 0:
        print(sum_-min(no_zero_list))
    else:
        print(0)