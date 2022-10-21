import io
import sys
from tkinter import N
from urllib.parse import non_hierarchical

_INPUT = """\
W
"""

sys.stdin = io.StringIO(_INPUT)

from collections import Counter

S=list(input())
S = Counter(S)

yoko = False
tate = False

if (S["S"] > 0 and S["N"] > 0) or (S["S"] == 0 and S["N"] == 0):
    tate = True

if (S["E"] > 0 and S["W"] > 0) or (S["E"] == 0 and S["W"] == 0):
    yoko = True

if tate and yoko:
    print("Yes")
else:
    print("No")