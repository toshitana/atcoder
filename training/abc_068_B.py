import io
import sys

_INPUT = """\
100
"""

sys.stdin = io.StringIO(_INPUT)

n = int(input())

max_n = 1
max_count = 0
for i in range(1,n+1):
    count = 0
    nn = i
    while(True):        
        if nn % 2 ==0:
            nn = nn//2
            count +=1
        else:
            break
    if  max_count < count:
        max_n = i
        max_count = count

print(max_n)
