import io
import sys

_INPUT = """\
1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000
"""

sys.stdin = io.StringIO(_INPUT)


li = list(map(int,input().split()))

print(((li[0] * li[1] * li[2])- (li[3] * li[4] * li[5]) )% 998244353)