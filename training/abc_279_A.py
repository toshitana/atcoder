import io
import sys

_INPUT = """\
wwwvvv
"""

sys.stdin = io.StringIO(_INPUT)

s = list(input())
sum_ = 0
sum_ += s.count("v") * 1
sum_ += s.count("w") * 2

print(sum_)