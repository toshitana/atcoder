import io
import sys

_INPUT = """\
4
2100 2500 2700 2700
"""

sys.stdin = io.StringIO(_INPUT)
n = int(input())
l = list(map(int,input().split()))

li = [0,0,0,0,0,0,0,0]
count = 0
for i in l:
    if i <= 399:
        li[0] =1
    if 400<= i <=799:
        li[1] =1
    if 800<= i <=1199:
        li[2] =1
    if 1200<= i <=1599:
        li[3] =1
    if 1600<= i <=1999:
        li[4] =1
    if 2000<= i <=2399:
        li[5] =1
    if 2400<= i <=2799:
        li[6] =1
    if 2800 <= i <=3199:
        li[7] =1
    if 3200<= i:
        count += 1

a = max(1,sum(li))
 
b = sum(li) + count
print(a,b)
# %%
