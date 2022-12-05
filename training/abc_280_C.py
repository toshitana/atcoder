import io
import sys

_INPUT = """\
vvwvw
vvwvwe
"""

sys.stdin = io.StringIO(_INPUT)

s=list(input())
t=list(input())

for i in range(len(s)):
    if s[i] != t[i]:
        print(i+1)
        exit()

print(len(t))