import io
import sys

_INPUT = """\
toyotasystems
toyotasystems
"""

sys.stdin = io.StringIO(_INPUT)

n = input()
s = input()

if s in n:
    print("Yes")
else:
    print("No")