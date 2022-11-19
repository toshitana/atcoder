import io
import sys

_INPUT = """\
abcdaxayz
"""

sys.stdin = io.StringIO(_INPUT)

s=list(input())



for i,v in enumerate(reversed(s)):
    if v == "a":
        print(len(s)-i)
        exit()

print(-1)