import sys
sys.setrecursionlimit(10 ** 6)

N, M = list(map(int, input().split()))
AB = [tuple(map(int, input().split())) for _ in range(M)]

#parentsリスト
p = [-1] * N

def root(x):
    if p[x] < 0:
        return x
    p[x] = root(p[x]) # 経路圧縮
    return p[x]

def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    p[x] += p[y]
    p[y] = x

ans = 0
for i in range(M):
    a, b = AB[i]
    a, b = a-1, b-1
    if root(a) == root(b):
        ans += 1
    else:
        unite(a, b)

print(ans)
