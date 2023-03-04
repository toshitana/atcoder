class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

n, m = map(int, input().split())
uf = UnionFind(n)
for i in range(m):
    u, v = map(int, input().split())
    uf.unite(u-1, v-1)

ans = True
for i in range(n):
    size = sum(uf.same(i, j) for j in range(n))
    edge_count = sum(1 for j in range(i, n) for k in range(j+1, n) if uf.same(i, j) and uf.same(i, k) and uf.same(j, k))
    if size != edge_count:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")
