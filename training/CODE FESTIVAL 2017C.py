import io
import sys

_INPUT = """\
10
90 52 56 71 44 8 13 30 57 84
"""

sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = list(map(int,input().split()))

odd = 0
even = 0

for i in A:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(3**len(A) - 2**even)