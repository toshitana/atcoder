import io
import sys

_INPUT = """\
10
979861204 57882493 979861204 447672230 644706927 710511029 763027379 710511029 447672230 136397527
"""

sys.stdin = io.StringIO(_INPUT)

n = int(input())
li = list(map(int,input().split()))

set_ = list(set(li))

set_.sort()

length = len(set_)

ans = []
for i in li:
    ans.append(length - set_.index(i)-1)

for i in range(n):
    print(ans.count(i))