import io
import sys

_INPUT = """\
280
"""

sys.stdin = io.StringIO(_INPUT)

n = int(input())













def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
a = factorization(n)

max_ = 0
for i in range(len(a)):
    if max_ <= a[i][0]*a[i][1]:
        max_ = a[i][0]*a[i][1]
        prime_pair = a[i]

def mmm(x):
    i = 1
    y = 0
    while x > y:
        y += i
        i += 1
    return i-1

mm = mmm(prime_pair[1])

if mm * prime_pair[0] < a[-1][0]*a[-1][1]:
    print(a[-1][0]*a[-1][1])
else:
    print(mm * prime_pair[0])