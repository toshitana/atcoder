import collections
n = int(input())
a = list(map(int, input().split()))

c = collections.Counter(a)
s = 0

for i in list(c.values()):
    s += i*(i-1) // 2

for i in a:
    print(s-(c[i]-1))