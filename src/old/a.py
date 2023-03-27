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

#頂点iから伸びる辺数を格納するリスト
degree = [0] * N

for i in range(M):
    a, b = AB[i]
    a -= 1
    b -= 1
    degree[a] += 1
    degree[b] += 1
    # 根が共通する場合にはUniteをすると閉路を形成してしまい、
    # 一直線上にならなくなるためNoと出力し終了します
    if root(a) == root(b):
        print("No")
        exit()
    # root(a)がroot(b)の親となるようにつなぎます
    unite(a, b)

if degree.count(1) == 2 and degree.count(2) == N - 2:
    print("Yes")
else:
    print("No")