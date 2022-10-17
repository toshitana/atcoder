import io
import sys

_INPUT = """\
9 10
0 3 5 7 100 110 200 300 311
"""

sys.stdin = io.StringIO(_INPUT)
N,T = map(int,input().split())
li = list(map(int,input().split()))

sum_ = 0
t_1 = 0

for i in li:
    if i - t_1 >= T or i == 0:
        #print("T",T)
        sum_ += T
        t_1 = i
    else:
        #print(T - max(0,T -(i - t_1)))
        sum_ += T - max(0,T -(i - t_1))
        t_1 = i
print(sum_)