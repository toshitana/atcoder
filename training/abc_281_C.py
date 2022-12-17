#%%
import io
from operator import index
import sys

_INPUT = """\
10 5678912340
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
"""
#%%
sys.stdin = io.StringIO(_INPUT)

N,T = map(int,input().split())
A = list(map(int,input().split()))
aaa = T // sum(A)
sumt = sum(A) * aaa
i = 0
while True:
    tmp = sumt
    sumt += A[i]
    if sumt >= T:
        sumt = tmp
        break
    i += 1
    #print(sumt)
    if i >= N:
        i = 0

print(i+1,abs(T-sumt))

# %%
