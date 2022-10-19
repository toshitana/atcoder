import io
import sys

_INPUT = """\
1 3 3
"""

sys.stdin = io.StringIO(_INPUT)

n,min_,max_ = map(int,input().split())

if min_ > max_:
    print(0)
    exit()


min_max_diff = max_ - min_
n_diff = n - 2

if min_ != max_ and n <= 1:
    print(0)
    exit()
print(1 + n_diff * min_max_diff)
