import io
import sys

_INPUT = """\
4
20 18 2 18
"""

sys.stdin = io.StringIO(_INPUT)

n = int(input())
card_list = list(map(int,input().split()))

card_list.sort(reverse=True)


a = 0
b = 0
for i,v in enumerate(card_list):
    if i % 2 ==0:
        a += v
    else:
        b += v

print(a - b)
