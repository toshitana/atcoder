import io
from operator import index
import sys

_INPUT = """\
8
"a,b"c,d
"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())

S = input()

# \括られた文字をカウントする
count = 0
result = ""
for c in S:
    if c == '"':
        count += 1

    if count % 2 == 0:
        # 現在の文字が括られた文字でない場合
        if c == ',':
            result += '.'
        else:
            result += c
    else:
        result += c

print(result)