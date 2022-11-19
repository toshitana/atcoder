import io
import sys

_INPUT = """\
fajsonlslfepbjtsaayxbymeskptcumtwrmkkinjxnnucagfrg
"""

sys.stdin = io.StringIO(_INPUT)
from collections import Counter
s=list(input())
s.sort()
s = Counter(s)

alphabet = list("abcdefghijklmnopqrstuvwxyz")

for i in alphabet:
    if s[i] == 0:
        print(i)
        exit()

print("None")