import io
import sys

_INPUT = """\
5
3 1 4 1 5
6
3 2
2 3 4
3 3
1 1
2 3 4
3 3
"""
from collections import defaultdict
sys.stdin = io.StringIO(_INPUT)

n = int(input())
li = [0]
li += list(map(int,input().split()))
q = int(input())
all_sum = 0
follows = defaultdict(int)
for i,v in enumerate(li):
    follows[i] = v

for _ in range(q):
    t = list(map(int,input().split()))
    if t[0] == 1:
        all_sum = t[1]
        follows = defaultdict(int)
    elif t[0] == 2:
        follows[(t[1])] += t[2]      
    else:
        print(all_sum + follows[(t[1])])
