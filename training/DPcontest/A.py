import io
import sys

_INPUT = """\
6
30 10 60 10 60 50
"""

sys.stdin = io.StringIO(_INPUT)

n=int(input())
A = list(map(int,input().split()))
A.append(1000)
A.append(1000)
dp = [1000] * (n+2)
dp[0] = 0
dp[1] = abs(A[0]-A[1])
for i in range(2,n):
    dp[i]=min(dp[i-1]+abs(A[i]-A[i-1]),dp[i-2]+abs(A[i]-A[i-2]))
print(dp[n-1])  