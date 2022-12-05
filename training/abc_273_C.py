from audioop import reverse
import io
import sys

_INPUT = """\
10
979861204 57882493 979861204 447672230 644706927 710511029 763027379 710511029 447672230 136397527
"""

sys.stdin = io.StringIO(_INPUT)
from collections import Counter
n = int(input())
li = list(map(int,input().split()))

li = Counter(li)

b = sorted(list(set(li)),reverse=True)

for i in b:
    print(li[i])

for i in range(n - len(li)):
    print(0)